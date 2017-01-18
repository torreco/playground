# Introduction to RxPY

## Topics Covered
* Observers
* Observables
* Operators
* Subjects

## Setup Guide
*Pre-requisites: git, python 2.7.X, virtualenv, pip (7.1.X recommended)* 

* Here are all the packages you'll need before you can
  proceed
  
  ```
  $ python -m pip install --upgrade pip
  $ python -m pip install --upgrade virtualenv
  ```

* Clone the repo from GitHub

  ```
  $ git clone https://github.com/torreco/playground.git
  $ cd playground/workshops/reactiveX
  ```
  
* Or fetch and pull

  ```
  $ cd playground/
  $ git checkout master
  $ git fetch --all; git pull
  $ cd workshops/reactiveX
  ```
  
* Create python virtual environment

  ```    
  $ virtualenv RxPY
  $ cd RxPY
  $ source bin/activate
  ```
  
* Install requirements using pip

  ```
  $ python -m pip install -U -r requirements.txt
  ```
  
* Run the notebook

  ```
  $jupyter notebook
  ```
