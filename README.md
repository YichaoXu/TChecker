# TChecker: Precise Static Inter-Procedural Analysis for Detecting Taint-Style Vulnerabilities in PHP Applications

TChecker is a static taint analysis tool for PHP applications. The key idea in TChecker is to iteratively construct call graph and precisely perform inter-procedural taint analysis. TChecker found 18 new vulnerabilities and two CVEs (CVE-2022-35212, CVE-2022-35213) were assigned.

**The author of the TChecker is [Luo Changhua](chluo@cse.cuhk.edu.hk) from CUHK. This repository is a forked version of the TChecker with a python wrapper script only for future research of JHU Seclab. We will not provide any suggestions about the usage, and we also make changes for the original codes. Please contact with the original author for usages details.**

## 1. Prerequisite

**ONLY php7.0 is supported. When compiling php-ast, only install phpize7.0 and do not install other versions, as this will cause incorrect header files to be included.**

### 1.1 Install OpenJDK 1.8

```bash 
# JVM 1.8 
# You can use the SDKMAN for mac and linux OS. See more information from the `https://sdkman.io`
$ sudo apt-get update
$ sudo apt-get install zip unzip wget
$ curl -s "https://get.sdkman.io" | bash
$ source "$HOME/.sdkman/bin/sdkman-init.sh"
$ sdk version # show something like "sdkman 5.18.0" 
$ sdk install java 8.0.302-open # install java 8.0.302-open (OpenJDK)
$ sdk default java 8.0.302-open 
```

### 1.2 Install PHP7.0 

Please following the steps from PHP official website, [install php7.0](https://prototype.php.net/versions/7.0/install/). We also provide you with the instructions for Ubuntu OS.

```bash 
# PHP 7.0.33 (10.Jan.2019)
$ sudo add-apt-repository ppa:ondrej/php
$ sudo apt-get update
$ sudo apt-get install php7.0-cli php7.0-fpm php7.0-opcache
```

### 1.3 Install php-cs-fix

We use the composer to install the php-cs-fix. Please following the instructions from the [getcomposer](https://getcomposer.org/download/). Again, we support the instructions for the Ubuntu users.

```bash 
$ wget https://raw.githubusercontent.com/composer/getcomposer.org/76a7060ccb93902cd7576b67264ad91c8a2700e2/web/installer -O - -q | php -- --quiet 
# Please ensure the path `/usr/local/bin/` in you $PATH. 
$ sudo mv composer.phar /usr/local/bin/composer
```

Another option is to use sudo apt-get install composer, but it will install an outdated version.

Then, you can use the composer to simply install the tool.


```bash
$ mkdir -p $HOME/php-cs-fixer
$ composer require --working-dir=$HOME/php-cs-fixer friendsofphp/php-cs-fixer:v3.16.0
```

### 1.4 Install phpjoern

Please exactly follow the instructions of PHPjoern [installation](https://github.com/malteskoruppa/phpjoern). For ubuntu user, use the following ones. 

First, you need to compile PHP-AST. 
```bash
# PHP-AST Installation
$ git clone https://github.com/nikic/php-ast
$ cd php-ast
$ git checkout 701e853
$ phpize
$ ./configure
$ make
$ sudo make install
```

Then, you need to configure the `php.ini` file to add the `php-ast` as a plugin of the PHP interpreter. 

```bash
# You need to first find out the path for php.ini 
$ php --info | grep "php.ini" # OUTPUT: "Loaded Configuration File => /etc/php/7.0/cli/php.ini"
$ echo 'extension=ast.so' >> /etc/php/7.0/cli/php.ini # Please notice that you should use you own path for `php.ini` 
```

Finally, you can clone the PHPJoern
```bash 
$ cd $HOME 
$ git clone https://github.com/malteskoruppa/phpjoern
```

## 2. Installation

### 2.1 Install TChecker 

Please clone this tchecker repository. Notice again, this is a forked version of the TChecker, and the original author is the [Luo Changhua](chluo@cse.cuhk.edu.hk). 

```bash
$ cd $HOME
$ git clone https://github.com/YichaoXu/TChecker.git
$ ./gradlew deploy -x test
```

### 2.2 Install wrapper 

Please ensure that you have python3 and pip3. Please also ensure that your pip3 path is configured correctly. 

```bash
$ cd $HOME/TChecker/wrapper
$ pip3 install -e .
```

## 3. How to use

### 3.1 Options of tchecker wrapper 


Please see the help doc by the `tchecker --help`. 
```bash 
$ tchecker --help
tchecker@seclab:~$ tchecker --help
Usage: tchecker [OPTIONS] TARGET

Arguments:
  TARGET  path to cached files  [required]

Options:
  --output PATH             path for outputs.  [default: tchecker.out]
  --verbose / --no-verbose  output more verbose information.   [default: no-
                            verbose]
  --help                    Show this message and exit.
```
This tool is a python wrapper of the TChecker, which is originally designed to process PHP code. Users are required to provide a TARGET argument, which is the path to the directory containing PHP files. The tool also provides some options:
* --output PATH: Specifies the output file path. The default is the tchecker.out file.
* --verbose / --no-verbose: Controls whether the tool outputs more detailed information. The default is no-verbose, which means no detailed information is output.
* --help: Displays help information and exits.


### 3.2 Example of the usage


Here is an example usage of the tchecker wrapper script:

```bash 
$ tchecker test.php --verbose
⚠️ Start TChecker for php file 'test.php'
  ✔️ PHP-CS-FIX Output:
    Loaded config default.
    Using cache file ".php_cs.cache".
    Fixed all files in 0.004 seconds, 12.000 MB memory used
  ✔️ PHP-JOERN Output:
    Parsing file /tmp/tchecker_1nneqmp8/test.php
    Done.
  ✔️ TChecker Output:
    @
    []
    @@@@
    @@@@@
    @@@@@@
    0 0 0
    {}
    all 0
    unneeded: 0
    initial: 1
    needed 1
⚠️ Outputs have already been generated under 'tchecker.out'
$ ls tchecker.out/
database.json  installed.json  nodes.csv  rels.csv  result.txt
```

In this example, the tchecker script is used to check a PHP file called test.php located in the current directory. The --verbose flag is used to provide more detailed output during the checking process.

The script starts by running the PHP-CS-FIXER tool to apply coding style fixes to the PHP code. It then runs the PHP-JOERN tool to generate an Abstract Syntax Tree (AST) representation of the PHP code in `test.php`. Finally, the tchecker script runs a custom analysis on the PHP code and generates output files in a directory called `tchecker.out`.

The output files include a database of the code structure, installed packages, node and relationship information, and a text file containing the results of the analysis.

Users can also specify an optional --output flag to specify a different output directory for the generated files. The --help flag can be used to display usage instructions for the script.

## Author
Please contact chluo@cse.cuhk.edu.hk for any questions.
