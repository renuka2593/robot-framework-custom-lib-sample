pipeline {
    agent any
    parameters {
        string(name: 'Year', defaultValue: '2025', description: 'Enter Year (default: 2025)')
        string(name: 'TestCases', defaultValue: '', description: 'Enter test cases to run (comma-separated, default runs all)')
    }
    stages {
        stage('Run All Robot Tests') {
            steps {
                script {
                    // Call the Python script to run all tests for all products and modes
                    def year = params.Year
                    def testCases = params.TestCases
                    
                    // If no specific test cases are provided, run all available tests
                    if (testCases == '') {
                        echo "Running all tests for all modes and products."
                    } else {
                        echo "Running selected tests: ${testCases}"
                    }

                    // Call Python script
                    echo "python3 run_robot_tests.py ${year} ${testCases}"
                }
            }
        }
    }
}
