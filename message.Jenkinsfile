pipeline {
    agent any

    triggers {
        // every two minutes
        cron('H/2 * * * *')
    }

    parameters {
        string(name: 'MESSAGE', defaultValue: 'Hello world!', description: 'Message to be displayed')
    }

    stages {
        stage('Say Message') {
            steps {
                echo "Message: ${params.MESSAGE}"
            }
        }
    }
}
