from env_interaction_sim import run_simulation

def run_single_simulation_experiments():
    MAX_MOVES_FOR_TESTS = 10  # Or another value you choose
    bot_configurations = [5, 10, 20, 30]  # Example list of bot counts

    print("=" * 40)
    print("Starting Simulation Experiments")
    print(f"Maximum moves per experiment: {MAX_MOVES_FOR_TESTS}")
    print("=" * 40)

    for num_bots_config in bot_configurations:
        print(f"\n[Experiment] Running with {num_bots_config} bots...")

        # Call the refactored main function with current parameters
        total_dirt_collected = run_simulation(NUM_BOTS=num_bots_config,
                                    MAX_MOVES=MAX_MOVES_FOR_TESTS)

        # Print the informative result for this run
        print(f"[Result]   Collected {total_dirt_collected} dirt with {num_bots_config} bots.")
        print("-" * 40)  # Separator for clarity

    print("\nAll experiments complete.")
    print("=" * 40)

run_single_simulation_experiments()