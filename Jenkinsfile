pipeline {
    agent any
    parameters {
        choice(name: 'Product', choices: ['AdobePremium', 'AdobeUltimate'], description: 'Select Product')
        choice(name: 'Mode', choices: ['Network'], description: 'Select Mode')
        string(name: 'Year', defaultValue: '2025', description: 'Enter Year (default: 2025)')
        string(name: 'BuildVersion', defaultValue: 'latest', description: 'Enter Build Version (default: latest)')
        string(name: 'TestCases', defaultValue: 'WebInstall,Download,DirectDownload,CustomInstall,CustomDeploy,UATTest', description: 'Enter test cases to run (comma-separated, default runs all)')
    }
    stages {
        stage('Run Selected Robot Tests') {
            steps {
                script {
                    def product = params.Product
                    def mode = params.Mode
                    def year = params.Year
                    def buildVersion = params.BuildVersion
                    def testCases = params.TestCases.split(',')

                    echo "Running tests for Product: ${product}, Mode: ${mode}, Year: ${year}, Build Version: ${buildVersion}"
                    echo "Selected test cases: ${testCases.join(', ')}"

                    testCases.each { testCase ->
                        echo "Running test case: ${testCase}"
                        echo "robot -v PRODUCT:${product} -v MODE:${mode} -v YEAR:${year} -v BUILD_VERSION:${buildVersion} tests/${testCase}.robot"
                    }
                }
            }
        }
    }
        post {
        always {
            archiveArtifacts artifacts: 'tests/output/*.xml, tests/output/*.html, tests/output/*.log', allowEmptyArchive: true
        }
    }
}
