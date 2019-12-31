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
  
  2、执行命令<br>
  ```
  C:\worksp> mvn archetype:generate -DgroupId=com.yiibai -DartifactId=NumberGenerator -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false
  ```
  
  3、在IntelliJ中加载maven、配置文件、本地库
  ![在intellij中加载maven]()
  
### 四
  


