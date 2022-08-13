# flask_kubernetes_using_nodeport

1) Build the docker image :

docker build -t="flask_app_with_nodeport" .



2) Create deployment file :

kubectl apply -f flask-deployment.yml   





3) Create services file :

kubectl apply -f flask-services.yml  



4) Get Node Port number using below command :

kubectl describe service flaskservice   




5) Get Node IP using below commands :

kubectl get nodes 
kubectl describe node minikube   


6) Verify the app :


12:11PM @Bharath ~ curl -i http://192.168.49.2:30937        
HTTP/1.1 200 OK
Server: gunicorn
Date: Sat, 13 Aug 2022 19:11:32 GMT
Connection: close
Content-Type: text/html; charset=utf-8
Content-Length: 78

This is a test webseite ! and served by host: flaskdeployment-58d4c6dddf-t2kqs%                                                                                                        12:11PM @Bharath ~ 
12:11PM @Bharath ~ curl -i http://192.168.49.2:30937
HTTP/1.1 200 OK
Server: gunicorn
Date: Sat, 13 Aug 2022 19:11:37 GMT
Connection: close
Content-Type: text/html; charset=utf-8
Content-Length: 78

This is a test webseite ! and served by host: flaskdeployment-58d4c6dddf-z4k6j%                                                                                                        12:11PM @Bharath ~ 




