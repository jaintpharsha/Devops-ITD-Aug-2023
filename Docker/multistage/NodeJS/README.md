# docker-multibuild-example
This is an demonstration project for docker multi build concept

Dockerfile_single
		
	To build node image as normal 
                docker build -f Dockerfile_single -t node_single .
	To run the container from above image
                docker run -it -d -p 3070:3070 node_single
		
There are two main problems with this build 
	 
	1) size of image and container. 
           Lets check the size of image: docker images 
	        - The size of our image is astonishingly high which is above 1.2GB. 	
		- We can’t ship the image of this size to production because of slower downloads 
		  because it takes longer than usual to download this image over the network.
	2) larger surface area.
           - Another problem is the larger surface area which is prone to attacks. 
           - We included npm dependencies and the entire Angular CLI library in the image which are
             unnecessary in the final image.
             
		 
Dockerfile multi-stage built

	- With multi-stage builds, we can use multiple FROM statements to build each phase. Every FROM   
	  statement starts with the new base and leave behind everything which you don’t need from the previous FROM statement.
	- We can have the same tiny image without much complexity
	  To build node image as multi-stage build 
		docker build -t node_multi .
	  To run the container from above image
		docker run -it -d -p 3070:3070 node_multi	
