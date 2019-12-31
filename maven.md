maven学习
===

### 一、maven的安装
  1、官网上下载安装包（apache-maven）<br>
  2、安装maven<br>
  3、配置环境变量：<br> 
  * 新建  M2_HOME : maven文件夹的路径
  * 新建  MAVEN_HOME : amven文件夹的路径
  * 修改  PATH : %M2_HOME%\bin

### 二、启用maven的代理访问（可选操作）
  1、打开maven的配置文件：maven文件夹 -- conf -- settings.xml<br>
  2、解开 ```<proxies></proxies>``` 中的注释<br>
  ```
  <proxies>
    <!-- proxy
     | Specification for one proxy, to be used in connecting to the network.
     |
    <proxy>
      <id>optional</id>
      <active>true</active>
      <protocol>http</protocol>
      <username>proxyuser</username>
      <password>proxypass</password>
      <host>proxy.host.net</host>
      <port>80</port>
      <nonProxyHosts>local.net|some.host.com</nonProxyHosts>
    </proxy>
    -->
  </proxies>
  ```
  3、在 ```<proxy></proxy>```中填写代理服务器的详细信息<br>
 
### 三、maven本地库
  Maven的本地资源库是用来存储所有项目的依赖关系(由Maven下载jar包和其他文件)。<br>
  1、自定义本地库的位置（在settings.xml文件中设置）<br>
  ```
  <!-- localRepository
   | The path to the local repository maven will use to store artifacts.
   |
   | Default: ${user.home}/.m2/repository
  <localRepository>/path/to/local/repo</localRepository>
  -->
  ```
  添加```<localRepository>自定义的本地库路径</localRepository>```<br>
  
  2、在IntelliJ中加载maven、配置文件、本地库<br>
  ![在intellij中加载maven](https://github.com/cy22117888/hello-world/blob/master/maven/intellij%E4%B8%AD%E5%8A%A0%E8%BD%BDmaven.PNG)
  
### 四、maven中央储存库
  在你的maven项目中，maven会根据pom.xml文件中的内容来加载该项目需要的依赖。<br>
  优先在本地库中查找依赖，当本地库中没有时，会默认到 http://search.maven.org 下载所需依赖<br>
  
  在settings.xml中自定义中央储存库（本例中设置为阿里云） 
  ![配置中央储存库](https://github.com/cy22117888/hello-world/blob/master/maven/setting%20global%20repository.PNG)
  
### 五、
  


