#!/usr/bin/python3
import glob
import importlib.util
import os
import re
import sys


def find_problem_folder(problem_number):
    matches = glob.glob(f"leetcode/*/{problem_number}_*/")
    if not matches:
        raise FileNotFoundError(f"No folder found for problem {problem_number}")
    return matches[0]


def load_solution_class(folder):
    path = os.path.join(folder, "main.py")
    spec = importlib.util.spec_from_file_location("solution", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.Solution()


def get_last_method(instance):
    # use last method
    # we can just "privatize" the other methods.
    return [fn for fn in dir(instance) if not fn.startswith("__")][-1]


def parse_leetcode_style_file(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()

    input_data = {}
    expected_output = None

    for line in lines:
        line = line.strip()
        if line.startswith("Input:"):
            input_str = line.replace("Input:", "").strip()
            pairs = re.split(r", (?=\w+ *=)", input_str)
            for pair in pairs:
                name, val = pair.split("=", 1)
                input_data[name.strip()] = eval(val.strip())
        elif line.startswith("Output:"):
            expected_output = eval(line.replace("Output:", "").strip())

    return input_data, expected_output


def run_all_tests(problem_number):
    folder = find_problem_folder(problem_number)
    tests_folder = os.path.join(folder, "tests")
    solution = load_solution_class(folder)
    method_name = get_last_method(solution)
    method = getattr(solution, method_name)

    input_files = sorted(glob.glob(os.path.join(tests_folder, "test*.txt")))
    if not input_files:
        print(f"⚠️ No test files found in {tests_folder}")
        return

    passed = 0
    total = 0

    for input_path in input_files:
        case_id = os.path.basename(input_path).replace("input", "").replace(".txt", "")
        input_data, expected_output = parse_leetcode_style_file(input_path)

        # deep copy inputs to preserve original data
        test_args = {
            k: v.copy() if isinstance(v, list) else v for k, v in input_data.items()
        }

        # default assumption: result is mutated input
        result = method(**test_args)
        total += 1
        if result == expected_output:
            print(f"✅ Test {case_id} passed")
            passed += 1
        else:
            print(f"❌ Test {case_id} failed")
            print(f"   Input   : {input_data}")
            print(f"   Expected: {expected_output}")
            print(f"   Got     : {result}")

    print(f"\n🧪 Summary: {passed}/{total} tests passed.")

    # Generate LeetCode URL
    folder_name = os.path.basename(os.path.normpath(folder))
    _, slug = folder_name.split("_", 1)
    leetcode_url = f"https://leetcode.com/problems/{slug}/description/"

    print(f"🔗 LeetCode Link: {leetcode_url}\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run.py <problem_number>")
    else:
        run_all_tests(sys.argv[1])
