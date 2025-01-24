pipeline {
    agent any
    
    parameters {
        choice(name: 'Bundle', choices: ['AdobePremium', 'AdobeUltimate'], description: 'Select the product bundle')
        choice(name: 'TestMode', choices: ['WebInstall', 'Download', 'DirectDownload', 'CustomInstall', 'CustomDeploy', 'UATTest'], description: 'Select test mode')
        string(name: 'BuildVersion', defaultValue: 'latest', description: 'Specify the build version')
    }
    
    environment {
        ROBOT_ENV = 'test'  // Define the environment for Robot Framework
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Pull your repository code
                checkout scm
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run Robot Framework tests
                    sh "robot --variable BUNDLE:${params.Bundle} --variable TEST_MODE:${params.TestMode} --variable BUILD_VERSION:${params.BuildVersion} path/to/tests"
                }
            }
        }
    }
}
