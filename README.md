External Cmds:
call external commands with '@' prefix

case insensitive.

command-syntax:
@[table-name] cmd
with no semicolon

cmds:
Create Table:
eg.: @create table

Add rows/records:
eg: @<table-name> add 69 rows
eg: @<table-name> add 69 stuff
eg: @<table-name> add 69

Echo/Select:
eg: @<table-name> echo //shows full table
eg: @<table-name> echo field1, field2,.... clause 1, clause 2,.... // select ki copy

eg: @<table-name> select //shows full table
eg: @<table-name> select field1, field2,.... clause 1, clause 2,.... // aakhir kyun bnaya ye?

Delete:
eg: @<table-name> delete <column> <value> //deletes records with specified column values
