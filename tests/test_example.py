import subprocess
import sys
from pathlib import Path

import pytest

import DIAMOnD

EXAMPLE = Path(__file__).resolve().parent.parent / 'Example'
PPI = str(EXAMPLE / 'PPI.txt')
SEEDS = str(EXAMPLE / 'seed_genes.txt')


def test_example(tmp_path):
    subprocess.run([sys.executable, '-m', 'DIAMOnD', PPI, SEEDS, '100'],
                   cwd=tmp_path, check=True, capture_output=True)

    with open(tmp_path / 'first_100_added_nodes_weight_1.txt') as fin:
        assert fin.readline() == '#rank\tDIAMOnD_node\tp_hyper\n'
        rows = [line.rstrip('\n').split('\t') for line in fin]

    _, seed_genes = DIAMOnD.read_input(PPI, SEEDS)
    assert [int(r[0]) for r in rows] == list(range(1, 101))
    assert len({r[1] for r in rows}) == 100
    assert not {r[1] for r in rows} & seed_genes
    assert all(0 <= float(r[2]) <= 1 for r in rows)

    # the first nodes are unambiguous (no ties in p-value)
    assert [r[1] for r in rows[:3]] == ['4758', '3073', '3074']
    assert [float(r[2]) for r in rows[:3]] == pytest.approx(
        [3.993956525332022e-07, 2.911000876883306e-08, 4.5586505962817925e-09])
