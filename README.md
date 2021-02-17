External Cmds:

call external commands with '@' prefix

case insensitive.

command-syntax:

@[table-name] [cmd]

//with no semicolon

cmds:

Create Table:

@create table

Add rows/records:

@table-name add 69 rows

@table-name add 69 stuff

@table-name add 69

@table-name add //to add indefinetely until '' value is given to a field. 

Echo/Select:

@table-name echo //shows full table

@table-name echo field1, field2,.... clause 1, clause 2,.... // select ki copy

@table-name select //shows full table

@table-name select field1, field2,.... clause 1, clause 2,.... // aakhir kyun bnaya ye?

Delete:

@table-name delete [column1] = [value1], [column2] = [value2].... //deletes records with specified column values, works with '=' as well

eg: @emp delete empid 69420 

Update:

@table-name update [condition/position] set [field1] = [value1], [field2] = [value2]....

Setting context:

you can set any table as current context with

@[table_name]

and then run above commands without '@table-name'

you get out of current context just enter '.' or '\\'
