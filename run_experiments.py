"""
Run CoT unfaithfulness experiments using inspect eval_set.

This script provides a flexible interface for running evaluations
with different configurations, making it easy to extend with new
prompting strategies or datasets.

Usage:
    # PR submission (limited samples)
    uv run python run_experiments.py --mode pr
    
    # Full replication
    uv run python run_experiments.py --mode full
    
    # Extensions with custom prompts
    uv run python run_experiments.py --mode extensions --prompt-style custom
"""

import argparse
from pathlib import Path
from inspect_ai import eval_set
from inspect_ai.util import list_tasks

def run_pr_submission():
    """Run limited evaluations for inspect_evals PR submission."""
    print("Running PR submission evaluations (50 samples)...")
    
    # Get tasks from your fork
    tasks = list_tasks("inspect_evals.cot_unfaithfulness")
    
    success, logs = eval_set(
        tasks=tasks,
        model=["openai/gpt-3.5-turbo"],
        log_dir="logs/pr_submission",
        task_args={"limit": 50},  # Limit samples for PR
    )
    
    if success:
        print("✓ PR submission evaluations completed successfully")
    else:
        print("✗ Some evaluations failed - check logs for details")
    
    return success

def run_full_replication():
    """Run complete replication with multiple models."""
    print("Running full replication experiments...")
    
    # Models from the original paper era and current equivalents
    models = [
        "openai/gpt-3.5-turbo",           # GPT-3.5
        "anthropic/claude-3-5-sonnet-20241022",  # Modern Claude
    ]
    
    tasks = list_tasks("inspect_evals.cot_unfaithfulness")
    
    success, logs = eval_set(
        tasks=tasks,
        model=models,
        log_dir="logs/full_experiments",
        max_tasks=4,  # Run up to 4 tasks in parallel
    )
    
    if success:
        print("✓ Full replication completed successfully")
        print(f"  Completed {len(logs)} evaluations")
    else:
        print("✗ Some evaluations failed")
        print("  Re-run this command to retry failed tasks")
    
    return success

def run_extensions(prompt_style: str = "standard", dataset: str = "bbh"):
    """
    Run extended experiments with different prompting strategies or datasets.
    
    This is a placeholder for future extensions - modify as needed.
    """
    print(f"Running extensions with prompt_style={prompt_style}, dataset={dataset}...")
    
    # Example: filter tasks or use custom task configurations
    tasks = list_tasks("inspect_evals.cot_unfaithfulness")
    
    # You could filter or modify tasks here based on your extensions
    # For example:
    # if prompt_style == "custom":
    #     tasks = [task for task in tasks if "custom" in task.name]
    
    success, logs = eval_set(
        tasks=tasks,
        model=["anthropic/claude-3-5-sonnet-20241022"],
        log_dir=f"logs/extensions_{prompt_style}_{dataset}",
        task_args={
            "prompt_style": prompt_style,
            "dataset": dataset,
        }
    )
    
    if success:
        print("✓ Extension experiments completed")
    else:
        print("✗ Some extension experiments failed")
    
    return success

def main():
    parser = argparse.ArgumentParser(
        description="Run CoT unfaithfulness replication experiments",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # PR submission
  python run_experiments.py --mode pr
  
  # Full replication
  python run_experiments.py --mode full
  
  # Extensions
  python run_experiments.py --mode extensions --prompt-style few-shot --dataset custom
        """
    )
    
    parser.add_argument(
        "--mode",
        choices=["pr", "full", "extensions"],
        default="full",
        help="Experiment mode to run"
    )
    
    # Extension arguments
    parser.add_argument(
        "--prompt-style",
        default="standard",
        help="Prompting style for extensions (e.g., few-shot, cot, custom)"
    )
    parser.add_argument(
        "--dataset",
        default="bbh",
        help="Dataset to use for extensions"
    )
    
    args = parser.parse_args()
    
    # Run the appropriate mode
    if args.mode == "pr":
        success = run_pr_submission()
    elif args.mode == "full":
        success = run_full_replication()
    else:  # extensions
        success = run_extensions(args.prompt_style, args.dataset)
    
    # Exit with appropriate code
    exit(0 if success else 1)

if __name__ == "__main__":
    main()
