
# Relational Database

## Management Systems (RDBMS)
### About RDBMS
- This refers to the software system that is used to interact and maintain a relational database.
- It stores data in a structured format using columns and rows
- The values within a table are related to each other.
- Tables can be related to other tables.
- It implements SQL (Structured Query Language) for querying and managing data within a relational database.
- RDMS supports the use of stored procedures within the database.
### About Keys
- Keys are used in order to uniquely identify rows within a table (i.e., a primary key).
- They can be used to form a link between tables (i.e., a foreign key).

---

# MySQL Installation on RedHat based system

## Installation Steps
1. Download the MySQL RPM bundle tar file from the MySQL Community Server downloads page.
```sh
# wget https://dev.mysql.com/get/Downloads/MySQL-8.0/mysql-8.0.15-1.el7.x86_64.rpm-bundle.tar
```
2. Extract the RPM files from the MySQL bundle tar file.
```sh
# tar -xvf mysql-8.0.15-1.el7.x86_64.rpm-bundle.tar
```
3. Install the MySQL server and dependencies using the rpm command.
```sh
# sudo rpm -Uvh mysql-community-{server,client,common,libs}-*
```
4. Start the MySQL server.
```sh
# sudo systemctl start mysqld
```
5. Log in to the MySQL server as the root user using the temporary password located in /var/log/mysqld.log
```sh
# sudo grep 'temporary password' /var/log/mysqld.log
# mysql -u root -p
```
6. Update the password for the root user.
```sql
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY'PASSWORD’;
mysql> exit;
```

## Secure Installation
1. Run the following command to launch the
secure installation:
```sh
# mysql_secure_installation
```
2. Answer the following questions to complete the secure installation:
- Change the password for root?
- Remove anonymous users?
- Disallow root login remotely?
- Remove test database and access to it?
- Reload privilege tables now?

---

# MySQL Installation on Debian based 

## Installation Steps
1. Download the MySQL APT repository configuration file from the MySQL APT Repository download page.
```sh
# wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
```
2. Install the downloaded release package for the MySQL server. In the package configuration window, ensure that MySQL Server and Cluster are set to mysql-8.0 and the MySQL Tools and Connectors is Enabled then hit OK.
```sh
# sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb
```
3. Resynchronize the package index files.
```sh
# sudo apt update
```
4. Install the MySQL server and dependencies. When prompted, enter a password, and then select Use Strong Password Encryption (RECOMMENDED).
```sh
# sudo apt install -y mysql-server
```
5. Validate that the MySQL server is running and then log in using the password created in prevuous step.
```sh
# sudo systemctl status mysql
# mysql -u root -p
mysql> exit
```

### Secure Installation
1. Run the following command to begin to launch the secure installation:
```sh
# mysql_secure_installation
```
2. Answer the following questions to complete the secure installation:
- Set up VALIDATE PASSWORD component?
- Set the level of the password validation password to STRONG: 2
- Change the password for root?
- Remove anonymous users?
- Disallow root login remotely?
- Remove test database and access to it?
- Reload privilege tables now?

---

# Creating Databases

## CREATE DATABASE Syntax:

CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name [create_specification] ...
create_specification:

[DEFAULT] CHARACTER SET [=] charset_name
| [DEFAULT] COLLATE [=] collation_name
| DEFAULT ENCRYPTION [=] {'Y' | 'N’}

Create a new database:
```sql
mysql> CREATE DATABASE db_name;
```
List available databases:
```sql
mysql> SHOW DATABASES;
```
Select database for use:
```sql
mysql> USE db_name;
```
Show current selected database:
```sql
mysql> SELECT DATABASE();
```
Select database when logging in to MySQL:
```sql
mysql> mysql -u user -p db_name;
```
### DROP DATABASE Syntax:

DROP {DATABASE | SCHEMA} [IF EXISTS] db_name

Delete an existing database:
```sql
mysql> DROP DATABASE db_name;
```
List available databases:
```sql
mysql> SHOW DATABASES;
```

## Using mysqladmin and mysqlshow from
the Command Line `mysqladmin` Syntax
```sh
shell> mysqladmin [options] command [command-arg] [command [command-arg]]
```
...
`mysqlshow` Syntax
```sh
shell> mysqlshow [options] [db_name [tbl_name [col_name]]]
```
Create a database:
```sh
# mysqladmin -u root -p create db_name
```
Drop a Database:
```sh
# mysqladmin -u root -p drop db_name
```
List available databases:
```sh
# mysqlshow -u root -p
```

---

# Creating Tables
## CREATE TABLE Syntax:

CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name (create_definition,...) [table_options] [partition_options]

Create a new table:
```sql
mysql> CREATE TABLE tbl_name (col_name col_def);
```
List tables:
```sql
mysql> SHOW TABLES [FROM db_name];
```
List columns in a table:
```sql
mysql> DESCRIBE tbl_name [db_name.tbl_name];
mysql> SHOW COLUMNS FROM tbl_name [FROM db_name];
```
List tables and columns using the `mysqlshow` command:
```sql
# mysqlshow -u NAME -p db_name
# mysqlshow -u NAME -p db_name tbl_name
```
List additional information about a table:
```sql
mysql> SHOW TABLE STATUS [FROM db_name];
```
Show statement that created a table:
```sql
mysql> SHOW CREATE TABLE tbl_name;
```

## Copying and Cloning Tables

Using CREATE TABLE...LIKE :
CREATE TABLE new_tbl LIKE orig_tbl;

Using CREATE TABLE...SELECT :
CREATE TABLE new_tbl [AS] SELECT * FROM orig_tbl;

DROP TABLE Syntax
DROP [TEMPORARY] TABLE [IF EXISTS] tbl_name [,tbl_name] ... [RESTRICT | CASCADE]

## Drop an existing table:

DROP TABLE tbl_name;
DROP TABLE db_name.tbl_name;

---

# Insert, View, and Delete Data
## INSERT Syntax
INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE] [INTO] tbl_name
[PARTITION (part_name [, part_name] ...)]
[(col_name [, col_name] ...)]
{VALUES | VALUE} (value_list) [, (value_list)] ...
[ON DUPLICATE KEY UPDATE assignment_list ]

### Insert rows into a table:
INSERT INTO tbl_name (col_name,col_name) VALUES
(val_list),(val_list);

### Using INSERT...SELECT:
INSERT INTO tbl_name (col_name,col_name) SELECT...
SELECT Syntax
SELECT [DISTINCT] select_expr [, select_expr] FROM tbl_ref
[WHERE where_cond]
[GROUP BY col|expr|positiion]
[HAVING where_cond]
[ORDER BY col|expr|positiion]
[LIMIT [offset,] row_count]
[INTO OUTFILE 'file_name’]

### List entries in a table;
SELECT * FROM tbl_name;
SELECT col1, col2 FROM tbl_name;

## DELETE Syntax
DELETE FROM tbl_name [WHERE where_cond] [ORDER BY ...] [LIMIT row_count]

### Delete a record from a table:
DELETE FROM tbl_name WHERE col = 'value'

--- 

# Connectors and APIs

### MySQL Connectors
- Connector/C - Provides a client library for C development and is used for C applications.
- Connector/C++ - Allows C++ applications to connect to MySQL.
- Connector/J - Implements the Java Database Connectivity (JDBC) API which allows Java applications to connect to MySQL.
- Connector/NET - Allows .NET applications to connect to MySQL. These applications can be written in any .NET supported language.
- Connector/ODBC - Provides support for connecting to MySQL through the Open Database Connective (ODBC) API.
- Connector/Python - Allows Python applications to connect to MySQL using a Python DB version 2.0 compliant API.

### MySQL APIs
- C API - Provides access to MySQL from C.
- PHP API - Provides access to MySQL from PHP. There are three API extensions available in PHP: mysqli , PDO_MYSQL , and mysql_xdevapi .
- Perl API - Provides access to MySQL from Perl. This requires the DBI module to be installed which provides a generic interface to access the database, as well as the Database Driver (DBD) module, DBD::mysql .
- Python API - Provides access to MySQL from Python. A third party driver, mySQLdb , may be used to provide MySQL support. Alternatively, the MySQL Connector/Python can be used as it provides an interface to the same Python API. Oracle also supports this connector.
- Ruby API - Provides access to MySQL from Ruby. Two APIs are available, the MySQL/Ruby API which is based on the libmysqlclient library, and the Ruby/MySQL API which is written to use the native MySQL network protocol.
- Tcl API - Provides access to MySQL from Tcl.

---

# Constraints
## MySQL Constraints
- NOT NULL - Prevents a column from storing a NULL value:
  - col_name data_type NOT NULL
- UNIQUE - Prevents any duplicate values from being entered into a column:
  - col_name data_type UNIQUE
- PRIMARY KEY - A column or set of columns used to uniquely identify the rows in a table:
  - col_name data_type PRIMARY KEY
- FOREIGN KEY - Creates a link between tables based on a column or columns within each. This allows related data to be cross-referenced in order to keep it
consistent:
  - FOREIGN KEY [index_name] (col_name,...)
  - REFERENCES tbl_name(col_name,...)

- CHECK - Determines whether a value is valid based on specific conditions:
  - col_name data_type CHECK(expr)

- DEFAULT - Allows a default value to be used for a column when no value is specified:
  - col_name data_type DEFAULT value

---

# Backups and Recovery

## Physical Backups

- They consist of copies of the database directories and files.
- Faster than logical backups.
- The size of the backup is more compact than a logical backup.
- Can range from single files to the entire data directory.
- Backups can be performed while the MySQL server is shutdown.
- Backups can be performed using system-level commands (i.e. cp, tar, rsync, etc.) for MyISAM tables or through the mysqlbackup tool for InnoDB tables (or any other tables).

## Logical Backups
- Backups are performed by querying the server to obtain the database structure and content information.
- Slower than physical backups.
- The size of the backup is larger than a physical backup.
- Can range from a single table to all the databases in the server.
- Backups must be performed while the server is running.
- Backups can be performed using the mysqldump tool or by performing a SELECT...INTO OUTFILE statement.

## Creating Backups in SQL Format
mysqldump syntax:
```sql
# mysqldump [arguments] > file_name
```
Backup all databases:
```sql
# mysqldump -u root -p --all-databases > dump.sql
```
Backup specific databases:
```sql
# mysqldump -u root -p --databases db1 db2 > dump.sql
```

Backup specific tables from a database:
```sql
# mysqldump -u root -p test tbl1 tbl2 > dump.sql
```
Restore from backup:
```sql
# mysql -u root -p < dump.sql
mysql> source dump.sql;
```
### Creating Backups in Delimited-Text Format

Create delimited-text file using `mysqldump` :
```sh
sudo mysqldump -u root -p --tab=/var/lib/mysql-files/ db_name [tbl_name]
```
Create delimited-text file using SELECT...INTO OUTFILE :
```sql
mysql> SELECT * FROM db_name.tbl_name INTO OUTFILE'/var/lib/mysql-files/dump.txt’;
```
Restore using delimited-text backups :
```sh
# mysql -u root -p db_name < tbl_name.sql
# mysqlimport -u root -p db_name tbl_name.txt
```
---