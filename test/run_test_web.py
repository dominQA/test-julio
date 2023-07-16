from behave.__main__ import main as behave_main
import subprocess


def run_behave_tests(tags=None):
    features_folder = "../test/features/destinia.feature"
    args = []
    if tags:
        args.append(f"--tags={tags}")
    args.append(features_folder)
    behave_main(features_folder)


if __name__ == '__main__':
    run_behave_tests("@frontoffice")

    subprocess.run(['allure', 'generate', 'allure-results', '-o', 'reports/allure-report', '--clean'], check=True)
    # el proceso de reporte no me funciona bien
