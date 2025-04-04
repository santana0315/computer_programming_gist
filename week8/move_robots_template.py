def move_robots(canvas, bots, passive_components, dirt_counter, moves, max_moves, move_delay):
    moves += 1
    print(f'Move count: {moves}')

    for bot in bots:
        agent = RobotAgent(bot)
        charger_intensity_left, charger_intensity_right = agent.sense_charger(passive_components)
        agent.transfer_function(charger_intensity_left, charger_intensity_right)
        agent.move(canvas, passive_components, dt=1.0)

        # Update bot state from agent (more efficient way)
        bot.x = agent.x
        bot.y = agent.y
        bot.theta = agent.theta
        bot.battery = agent.battery
        bot.sensor_positions = agent.sensor_positions

        # Dirt collection
        passive_components = agent.collect_dirt(canvas, passive_components, dirt_counter)

    if moves > max_moves:
        print(f"Total dirt collected after {max_moves} moves: {dirt_counter.dirt_collected}")
        sys.exit()  # Or window.destroy() to close the window

    canvas.after(move_delay, move_robots, canvas, bots, passive_components, dirt_counter, moves, max_moves, move_delay)
