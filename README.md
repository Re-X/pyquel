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

To add records from another text file (comma separated values):

@table-name add csv [filepath]

Echo/Select:

@table-name echo //shows full table

@table-name echo field1, field2,.... clause 1, clause 2,.... // select ki copy

@table-name select //shows full table

@table-name select field1, field2,.... clause 1, clause 2,.... // aakhir kyun bnaya ye?

Delete:

@table-name delete [condition(s)] //deletes records with specified column values, works without '=' as well

eg: @emp delete empid = 69420 

Update:

@table-name update [condition(s)/position(s)] set [field1] = [value1], [field2] = [value2]....

Truncate:

@table-name truncate

Setting context:

you can set any table as current context with

@[table_name]

and then run above commands without '@table-name'

to get out of current context just enter '.' or '\\'

To use system commands:

enter cmds with prefix '!'

eg: !net start mysql80

eg: !python //to literally run python, exit with exit()

To run as admin: 
!admin


