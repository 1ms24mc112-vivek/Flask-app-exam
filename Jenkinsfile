pipeline{
	agent any
	environment{
	IMAGE_NAME="docker/repo"
	}
	stages{
		stage('Checkout'){
			steps{
				git branch:'main' , url:'<repo'
			}
		}
		
		stage('Build DockerImage'){
			steps{
				scripts{
					docker.build("${IMAGE_NAME}:latest")
				}
			}
		}
			
		stage('Push Docker Image to DockerHUB'){
			steps{
                                scripts{
                                        docker.withRegistry('http://index.docker.io/v1','dockerhub'){
						dockerImage.push("latest")
                                }
                        }

		}
	}
}
}

