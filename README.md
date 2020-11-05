# Coronavirus-Tracker
introduce: the objective of this project is use bokeh to visualize the data of coronavirus.

# Execute steps
1 first step
Clone files in this github reposiroty to local machine.
Create new environment on machine named dsci560H5 under the directory of clone file.
![](https://github.com/2133649586/imag/blob/main/%E6%88%AA%E5%B1%8F2020-11-05%2013.14.53.png)

2 second step
Activate the environment and install ONLY the dependencies you need to execute the random
![](https://github.com/2133649586/imag/blob/main/%E6%88%AA%E5%B1%8F2020-11-05%2013.15.15.png)
![](https://github.com/2133649586/imag/blob/main/%E6%88%AA%E5%B1%8F2020-11-05%2013.15.40.png)
![](https://github.com/2133649586/imag/blob/main/%E6%88%AA%E5%B1%8F2020-11-05%2013.16.07.png)

3 third step
Execute the resulting.py by bokeh serve under the fold with resulting.py file
![](https://github.com/2133649586/imag/blob/main/%E6%88%AA%E5%B1%8F2020-11-05%2013.23.49.png)


# Dokeh
1. you need ensure that the docker desktop is already download in you local machine.
  download address: https://www.docker.com/products/docker-desktop.
2. clone the file from github.
  RUN: git clone https://github.com/2133649586/Coronavirus-Tracker.git
3. build image under directory the file you download.
  RUN: docker build -t covid
4. run the image in terminal with port(5006)
  RUN: docker run -p 5006:5006 -it covid
5. copy the link to browser, the web will show the result
  http://localhost:5006/resulting
  

# result show
this area show the source of data, and the last update date of these data sets.
![](https://github.com/2133649586/imag/blob/main/%E6%88%AA%E5%B1%8F2020-11-05%2015.25.42.png)

you can select certain date.
![](https://github.com/2133649586/imag/blob/main/%E6%88%AA%E5%B1%8F2020-11-05%2015.25.55.png)

it shows that the increased number of confirmed cases in select date.
![](https://github.com/2133649586/imag/blob/main/%E6%88%AA%E5%B1%8F2020-11-05%2015.26.05.png)

this is datatable and visualization, it shows death percent, confirm percent and population percent by races.
![](https://github.com/2133649586/imag/blob/main/%E6%88%AA%E5%B1%8F2020-11-05%2015.26.13.png)
![](https://github.com/2133649586/imag/blob/main/%E6%88%AA%E5%B1%8F2020-11-05%2015.26.31.png)
