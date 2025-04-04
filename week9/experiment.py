from env_interaction_sim import run_simulation

def run_single_simulation_experiments(bot_counts, max_moves):
    """
    Runs a single simulation for each bot configuration.
    """
    for num_bots in bot_counts:
        collected_dirt = run_simulation(NUM_BOTS=num_bots, MAX_MOVES=max_moves)
        print(f"[Single] {num_bots} bot(s): Collected {collected_dirt} dirt.")


def run_multiple_trials(bot_counts, num_trials, max_moves):
    """
    Runs multiple trials per bot configuration.
    """
    for num_bots in bot_counts:
        for trial_index in range(1, num_trials + 1):
            collected_dirt = run_simulation(NUM_BOTS=num_bots, MAX_MOVES=max_moves)
            print(f"[Trial] {num_bots} bot(s), Trial {trial_index}: {collected_dirt} dirt")


if __name__ == "__main__":
    bot_counts = [1, 5, 10, 20]       # List of bot numbers to test
    num_trials = 3                    # Number of trials per bot configuration
    max_moves_per_run = 200           # Fixed maximum moves for consistency

    run_single_simulation_experiments(bot_counts, max_moves_per_run)
    run_multiple_trials(bot_counts, num_trials, max_moves_per_run)
