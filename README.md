# Chain-of-Thought Unfaithfulness: A Replication Study

Replication and extension of Turpin et al. (2023) on unfaithfulness in Chain-of-Thought prompting. Contributions by members of the Evals Reading Group.

## Authors

- Author 1 (Institution)
- Author 2 (Institution)
- Author 3 (Institution)

## Setup

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and install
git clone https://github.com/mjbroerman/cot_unfaithfulness_replication.git
cd cot_unfaithfulness_replication
uv sync

# Configure API keys
cp .env.example .env
# Edit .env with your keys
```

## Run Experiments

```bash
# PR submission (limited, tracked in git)
uv run python run_experiments.py --mode pr

# Full replication
uv run python run_experiments.py --mode full

```

## View Results

```bash
quarto render
```

## Citation

```bibtex
@misc{author2025cot,
  title={Chain-of-Thought Unfaithfulness: A Replication Study},
  author={Author 1 and Author 2 and Author 3},
  year={2025},
  howpublished={\url{https://github.com/mjbroerman/cot_unfaithfulness_replication}}
}
```

## License

[MIT/Apache-2.0/CC-BY-4.0]

## Acknowledgements

This project was supported by BlueDot Impact and the organizers of the Evals Reading Group.