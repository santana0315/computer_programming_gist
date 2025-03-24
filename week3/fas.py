# import sys
#
# student_code = """{{ STUDENT_ANSWER | e('py') }}"""
# student_namespace = {}
#
# # Execute student code
# exec(student_code, student_namespace)
#
# # Capture printed output
# from io import StringIO
# sys.stdout = StringIO()
# exec(student_code, student_namespace)
# output = sys.stdout.getvalue().strip()
#
# expected_output = (
#     "Robot robot1 is having the color black given that the condition is True.\n"
#     "Robot robot2 is having the color black given that the condition is True."
# )
#
# assert output == expected_output, f"Expected:\n{expected_output}\nGot:\n{output}"


# Define the color sets for different parts of the robots
colors = dict(
    robot1=dict(
        wheel_color_left="red",
        wheel_color_right="green",
        sensor_color="gold",
        light_color="yellow",
        body_color="blue",
    ),
    robot2=dict(
        wheel_color_left="orange",
        wheel_color_right="purple",
        sensor_color="silver",
        light_color="pink",
        body_color="cyan",
    ),
)

# Define a list of robot configurations
robot_configurations = [
    dict(id="robot1", center_x=327),
    dict(id="robot2", center_x=627)
]

# Set the condition
condition = False  # Change to False to test the first branch

# Iterate through each robot configuration
for config in robot_configurations:
    robot_colors = colors[config['id']]
    if condition:
        body_color = "black"
    elif not condition and config['id'] == 'robot1':
        body_color = "green"
    else:
        body_color = robot_colors["body_color"]

    print(f"Robot {config['id']} is having the color {body_color} given that the condition is {condition}.")
