.. highlight:: text

=======================================
Appendix C -- Non-portable SQL Features
=======================================

Not all SQL DBMSs are created equal. This Appendix lists the areas for which 
the SQL Standard provides no standardized solution for a DBMS, i.e.: the 
following areas are all labeled either "implementor-defined" or "implementor- 
dependent" in the Standard. Thus, valid syntax and/or the expected response 
will vary from one DBMS to another -- keep this in mind when writing your 
applications. 

.. rubric:: Table of Contents

.. contents::
    :local:

Implementation-Defined Features
===============================

The SQL Standard requires a SQL DBMS to define and document how it will handle
each of these features.

*Overall Method of SQL Support*
-------------------------------

The exact SQL syntax and method for accessing SQL-data supported by a DBMS is
non-standard for four reasons:

1. The SQL Standard allows implementors to choose to support either one
   of the following options for SQL conformance: Core SQL or Enhanced SQL.

2. The SQL Standard allows implementors to choose to support either one
   or more of the following options for binding style: Module Language, Embedded
   Syntax or Direct SQL Invocation.

3. The SQL Standard contains numerous non-standardized areas where
   implementors are required to decide upon appropriate responses on their own:
   the "implementor-defined" and "implementor-dependent" areas contained in the
   Standard.

4. The SQL Standard allows implementors to provide options for processing 
   database operations that the Standard does not address (e.g.: a ``CREATE 
   INDEX`` statement), as well as allowing implementors to provide options for 
   processing Standard-defined SQL in a non-conforming manner. To quote the 
   Standard: "An [SQL-]implementation remains conforming even if it provides 
   user options to process nonconforming SQL language or to process conforming 
   SQL language in a nonconforming manner." 

*Connection and Session Results*
--------------------------------

The result of executing ``CONNECT TO`` is non-standard because the SQL Standard
allows implementors to choose to support either one of the following options:

1. a DBMS may allow the establishment of only one SQL-session at a time, or

2. a DBMS may support multiple concurrent SQL-sessions.

A DBMS's default SQL-session and initial default SQL-Connection are non-
standard because the SQL Standard requires implementors to choose their own
initial default <Connection name>.

The effect of ``CONNECT TO DEFAULT;`` is non-standard because the SQL Standard
requires implementors to define what the default SQL-Connection and the
default SQL-server are.

A <Connection name> must be a <regular identifier> or a <delimited identifier>
that is no more than 128 octets in length, but the value of a valid
<Connection name> is non-standard because the SQL Standard requires
implementors to define what a valid <Connection name> may be and what
Character set <Connection name>s belong to.

A DBMS's initial default <AuthorizationID> is non-standard because the SQL
Standard requires implementors to choose their own initial default
<AuthorizationID>.

The effect of omitting the optional ``USER`` clause from a ``CONNECT`` statement
is non-standard because the SQL Standard requires implementors to define their
own initial default SQL-session <AuthorizationID>.

Whether the <user name> in a ``CONNECT`` statement must be identical to the 
Module <AuthorizationID> is non-standard because the SQL Standard requires 
implementors to define whether the two must match. 

A DBMS's initial default Catalog is non-standard because the SQL Standard
requires implementors to choose their own initial default <Catalog name>.

A DBMS's initial default Schema is non-standard because the SQL Standard
requires implementors to choose their own initial default <Schema name>.

A DBMS's initial default Character set is non-standard for two reasons:

1. The SQL Standard requires implementors to choose their own initial
   default <Character set name>.

2. The SQL Standard requires implementors to define the character
   repertoire for their initial default Character set.

A DBMS's initial default time zone offset is non-standard because the SQL
Standard requires implementors to define their own initial default time zone
offset.

The result of executing ``SET SESSION AUTHORIZATION`` is non-standard for two
reasons:

1. Although it is mandatory to support the use of ``SET SESSION
   AUTHORIZATION`` at the start of a SQL-session, the SQL Standard allows
   implementors to decide whether to allow the SQL-session default
   <AuthorizationID> to be changed at any other time.

2. For DBMSs that allow the use of ``SET SESSION AUTHORIZATION`` at other
   times, the SQL Standard allows implementors to define when exactly when the
   SQL-session default <AuthorizationID> may also be changed.

SQL does not include any ``CREATE CLUSTER``, ``OPEN CLUSTER``, ``ADD TO 
CLUSTER`` or ``DROP CLUSTER`` statements. The method you'll use to access a 
Cluster with your DBMS is thus non-standard because the SQL Standard requires 
implementors to define what the physical aspects of a Cluster are, whether any 
Catalog can be part of more than one Cluster at a time, how a Cluster comes 
into being, how it may be accessed and how it may be destroyed. 

SQL does not include any ``CREATE CATALOG``, ``OPEN CATALOG`` or ``DROP 
CATALOG`` statements. The method you'll use to access a Catalog with your DBMS 
is thus non-standard because the SQL Standard requires implementors to define 
how a Catalog comes into being, how it may be accessed and how it may be 
destroyed. 

The total number of Views in ``INFORMATION_SCHEMA``, and their exact 
definition, is non-standard because the SQL Standard allows implementors to add 
additional Views, as well as to add additional Columns to the Standard-defined 
Views, to describe additional, implementation-defined features. 

*Parsing/Display*
-----------------

A newline character, or end-of-line marker, is non-standard because the SQL
Standard requires implementors to define which white space characters their
parsers will recognize as newline characters.

The logical representation of the null value is non-standard because the SQL
Standard requires implementors to define the character used to display the
null value.

Either a ``NULL`` is greater than all non-null values or a ``NULL`` is less 
than all non-null values -- it's non-standard because the SQL Standard requires
implementors to define whether ``NULL``\s sort high or low.

*Names*
-------

An <SQL-server name> must be unique (for all Clusters) within an SQL-
environment, but is non-standard for two reasons:

1. The SQL Standard requires implementors to define what constitutes a
   valid <SQL-server name>.

2. The SQL Standard requires implementors to define the Character set
   that the characters of a <SQL-server name> belong to.

An <AuthorizationID> is non-standard for four reasons:

1. The SQL Standard requires implementors to define what constitutes a
   valid <AuthorizationID>.

2. The SQL Standard requires implementors to define their own method for
   mapping <AuthorizationID>s to users.

3. The SQL Standard requires implementors to define their own method for
   creating an <AuthorizationID>. SQL does not include a ``CREATE 
   AUTHORIZATIONID`` statement.

4. The SQL Standard requires implementors to define their own method for
   dropping an <AuthorizationID>. SQL does not include a ``DROP 
   AUTHORIZATIONID`` statement.

<Connection name>s are non-standard for two reasons:

1. The SQL Standard requires implementors to define what constitutes a
   valid <Connection name>.

2. The SQL Standard requires implementors to define the Character set
   that the characters of a <Connection name> belong to.

A <Catalog name> is a <regular identifier> or <delimited identifier> that is
unique (for all Catalogs) within the Cluster it belongs to, but is non-
standard because the SQL Standard requires implementors to define all valid
<Catalog name>s.

*Defining <literal>s*
---------------------

A national <character string literal> belongs to a Character set which is the
same Character set used for ``NCHAR`` and ``NCHAR VARYING`` <data type>s but is 
non-standard for two reasons:

1. The SQL Standard requires implementors to define the Character set
   that the characters of a national <character string literal> belong to.

2. The SQL Standard requires implementors to define the character
   repertoire for their national <character string literal> Character set.

The maximum size of a <time value>'s fractional seconds may not be less than 6
digits but is non-standard because the SQL Standard requires implementors to
define the maximum fractional seconds precision.

The maximum length of a <time literal> may not be less than 15 characters but
is non-standard because the SQL Standard requires implementors to define the
maximum size of a <time value>'s fractional seconds precision.

The allowable range for a <time value> must include, at a minimum, all times
from: ``TIME '00:00:00.0'`` to: ``TIME '23:59:61.999999'`` but the exact range 
of valid values is non-standard because the SQL Standard requires implementors
to define the maximum size of a <time value>'s fractional seconds precision.

The maximum length of a <timestamp literal> may not be less than 26 characters
but is non-standard because the SQL Standard requires implementors to define
the maximum size of a <time value>'s fractional seconds precision.

The allowable range for a <timestamp value> must include, at a minimum, all 
timestamps from: ``TIMESTAMP '0001-01-01 00:00:00.0'`` to: ``TIMESTAMP 
'9999-12-31 23:59:61.999999'`` but the exact range of valid values is 
non-standard because the SQL Standard requires implementors to define the 
maximum size of a <time value>'s fractional seconds precision. 

The maximum "start datetime" precision for an <interval qualifier> may not be
less than 2 digits but is non-standard because the SQL Standard requires
implementors to uefine the maximum leading precision.

The maximum fractional seconds precision for an <interval qualifier>'s "start
datetime" value or "end datetime" value of ``SECOND`` may not be less than 6 
digits but is non-standard because the SQL Standard requires implemented
Privileges held on the Module by any other <AuthorizationID> are also revoked.

All SQL routines, Triggers, Views and Constraints that depend on the Module
are dropped with a ``CASCADE`` drop behaviour.

*BEGIN ... END: Compound Statement*
-----------------------------------

Advance warning: ``BEGIN ... END`` has several optional clauses. We are going 
to start with the simplest form, and examine the options in following sections. 

In its simplest form, ``BEGIN ... END`` in SQL serves the same purpose as 
"begin...end" in Pascal or "{...}" in C. ``BEGIN ... END`` encloses a sequence 
of statements which are part of the same syntactical unit: a compound 
statement. The simplest required syntax is: 

::

    BEGIN
       [ <SQL statement>; ... ]
    END

Here's a simple example:

::

   BEGIN
       INSERT INTO Table_1 VALUES (5);
       INSERT INTO Table_2 VALUES (6);
   END

ATOMIC Statements
_________________

A slightly more complicated form of a compound statement has one extra optional
clause: ``[NOT] ATOMIC``. The required syntax is:

::

    BEGIN [ [ NOT ] ATOMIC ]    /* whether compound statement is atomic */
      [ <SQL statement>; ... ]
    END

If ``ATOMIC`` is specified, the compound statement may not contain ``COMMIT`` 
or ``ROLLBACK``. If you omit the clause, it defaults to ``NOT ATOMIC``: the 
compound statement may contain ``COMMIT`` or ``ROLLBACK``. Here's an example: 

::

   BEGIN ATOMIC
      INSERT INTO Table_1 VALUES (5);
      INSERT INTO Table_2 VALUES (6);
   END

We've already discussed the idea that transactions are atomic, and individual 
SQL statements are atomic. Compound SQL statements can be atomic too, provided 
that they are explicitly designated by the <keyword> ``ATOMIC``. Thus, in the 
above example, if the first ``INSERT`` statement succeeds but the second 
``INSERT`` statement fails, then the effects of the first ``INSERT`` is 
cancelled. It's as if there was a savepoint at the beginning of the compound 
statement and a ``ROLLBACK TO SAVEPOINT`` was executed when the second 
``INSERT`` failed. 

Variables
_________

A slightly more complicated form of a compound statement has one more optional
clause: a variable declaration list. The required syntax is:

::

    BEGIN [ [ NOT ] ATOMIC ]
      [ <variable declaration>; ... ]     /* variable-declaration list */
      [ <SQL statement>; ... ]
    END
    
   <variable declaration> ::=
   DECLARE <SQL variable name> <data type> [ DEFAULT default value ]

Here's an example:

::

   BEGIN ATOMIC
     DECLARE v1 CHAR(5);                          /* variable declaration */
     DECLARE v2,v3,v4 SMALLINT;                   /* variable declaration */
     DECLARE v5 DATE DEFAULT DATE '1993-01-01';   /* variable declaration */
     SELECT * INTO v1,v2,v3,v4 FROM Table_1;      /* statement */
     INSERT INTO Table_2 VALUES (v1,v2,v3,v4,v5); /* statement */
   END

.. CAUTION::

   Don't get confused by the similarity to a <Column definition>. A variable 
   definition can contain ``ONLY`` a <data type> and (optionally) a ``DEFAULT`` 
   clause. It cannot contain a <Domain name>, a <Constraint> or a ``COLLATE`` 
   clause. 

In our example we defined five variables: ``v1``, ``v2``, ``v3``, ``v4``, 
``v5``. ``BEGIN ... END`` defines a "local scope", which means that *(a)* these 
variable names have no meaning outside the compound statement, *(b)* the values 
in these variables are not saved when the compound statement ends and *(c)* the 
values in these variables are not reset by execution of a ``ROLLBACK`` 
statement, because variables are not part of the database. 

The example uses the first four variables as targets in a singleton ``SELECT`` 
statement. It also uses all five variables as sources in an ``INSERT`` 
statement. Variables can be used in all sorts of <value expression>s. Variables 
are extremely useful for temporary storage, and it's a wonder that most SQL 
implementations get along without them. The designers of SQL don't give us the 
option of using variables for persistent storage: we're supposed to use Base 
tables for that. 

Assignment Statements
_____________________

Assignment statements begin with the <keyword> ``SET`` -- but don't call them 
"``SET`` statements", to avoid confusion with non-PSM statements that also 
begin with ``SET``. Assignment statements are syntactically similar to the 
``SET`` clauses used in ``UPDATE`` statements. Here is the required syntax: 

::

    SET
       <target>     /* where the value goes to; usually a variable */
       =
       <source>     /* where the value comes from; an expression */

In theory the <target> doesn't have to be a variable -- it could be a
parameter or a "host variable" -- but normal programs will take the form
"<variable> = <expression>". Here are some examples:

::

   SET v1 = 5
   SET v1 = (v2+7)/5
   SET v1 = NULL
   SET v1 = column_1

Cursors
_______

A slightly more complicated form of a compound statement has one more optional
clause: a Cursor declaration list. The required syntax is:

::

    BEGIN [ [ NOT ] ATOMIC ]
      [ <variable declaration>; ... ]
      [ DECLARE CURSOR statement; ... ]      /* Cursor-declaration list */
      [ <SQL statement>; ... ]
    END

The mechanics of Cursors are the same for PSM as they are for embedded SQL and
for SQL/CLI. Here's an example:

::

   BEGIN
     DECLARE v1 SMALLINT;             /* variable-declaration */
     DECLARE cc CURSOR FOR
        SELECT column_1 FROM Table_1; /* Cursor-declaration */
     OPEN cc;                         /* statement */
     FETCH cc INTO v1;                /* statement */
     CLOSE cc;                        /* statement */
     INSERT INTO Table_2 VALUES (v1); /* statement */
   END

Objects that you declare in a compound statement have "local scope", so the
<Cursor name> in this example -- cc -- can only be  used by SQL statements
within the ``BEGIN ... END``. The example could be replaced with this SQL 
statement:

::

    INSERT INTO Table_2 SELECT column1 FROM Table_1;

if there is only one row in ``TABLE_1``.

Conditions
__________

A slightly more complicated form of a compound statement changes the optional
variable declaration clause: instead of a variable declaration list, ``BEGIN ...
END`` actually allows a variable or condition declaration list, so that you can
declare conditions as well as variables. The required syntax is:

::

    BEGIN [ [ NOT ] ATOMIC ]
      [ <variable | condition declaration>; ... ] /* variable-or-condition
    declaration list */
      [ DECLARE CURSOR statement; ... ]
      [ <SQL statement>; ... ]
    END
   <condition declaration> ::=
      DECLARE <condition name> CONDITION [ FOR <sqlstate value> ]

**Quick review:** An ``SQLSTATE`` value is a 5-character status code string. 
Upon completion of any SQL statement, there will be a status code in 
``SQLSTATE``, which is the main diagnostic field. Typical values are ``'01006' 
(warning-privilege not revoked)``, ``'22012' (data exception-division by 
zero)``, ``'42000' (syntax error or access violation)``. You'll find a complete 
list of ``SQLSTATE`` values in our chapter on SQL/CLI diagnostics. 

Here's an example of the latest form of ``BEGIN ... END``:

::

   BEGIN ATOMIC
     DECLARE v1 SMALLINT;                          /* variable-declaration */
     DECLARE warning_revoke CONDITION FOR '01006'; /* condition declaration */
     DECLARE divide_by_zero CONDITION FOR '22012'; /* condition declaration */
     DECLARE syntax_error CONDITION FOR '42000';   /* condition declaration */
     DECLARE cc CURSOR FOR
        SELECT column_1 FROM Table_1;              /* Cursor-declaration */
     OPEN cc;                                      /* statement */
     FETCH cc INTO v1;                             /* statement */
     CLOSE cc;                                     /* statement */
     INSERT INTO Table_2 VALUES (v1);              /* statement */
     INSERT INTO Table_1 VALUES (0);               /* statement */
     INSERT INTO Table_2 VALUES (1);               /* statement */
   END

In this example, we have simply given condition names to three of the possible
``SQLSTATE`` values.

Handlers
________

A slightly more complicated form of a compound statement adds another optional
clause: a handler declaration list. The required syntax is:

::

    BEGIN [ [ NOT ] ATOMIC ]
      [ <variable | condition declaration>; ... ]
      [ DECLARE CURSOR statement; ... ]
      [ <handler declaration>; ...]               /* handler-declaration list */
      [ <SQL statement>; ... ]
    END
    
    <handler declaration> ::=
    DECLARE <handler type> HANDLER FOR <condition value list> <handler action>
    
    <handler type> ::= {CONTINUE | EXIT | UNDO }
    
    <handler action> ::= <SQL statement>
    
    <condition value list> ::= <condition value> [ {,<condition value>}... ]
    
    <condition value> ::=
    <sqlstate value>| <condition name>| SQLEXCEPTION | SQLWARNING | NOT FOUND

The following example contains three handlers. The first is for an ``SQLSTATE``
value, the second is for a condition name and the third is for any warning
(i.e.: any ``SQLSTATE`` in class ``'01'``).

::

  BEGIN
    DECLARE constraint_error CONDITION FOR '23000';/* condition declaration */
    DECLARE v1 CHAR(5) DEFAULT 'Okay!';            /* variable declaration */
    DECLARE CONTINUE HANDLER FOR '22003'           /* handler declaration */
       SET v1 = 'Ovflw';
    DECLARE CONTINUE HANDLER FOR constraint_error  /* handler declaration */
       SET v1 = 'c-err';
    DECLARE CONTINUE HANDLER FOR SQLWARNING        /* handler declaration */
       SET v1 = '?????';
    INSERT INTO Table_1 VALUES (99999);            /* statement */
    INSERT INTO Table_2 VALUES (v1);               /* statement */
  END

To see the effect of these handlers, consider what will happen with the SQL
statement:

::

   INSERT INTO Table_1 VALUES (99999);

If this SQL statement fails due to overflow, then variable ``v1`` gets 
``'Ovflw'``; if it fails due to an integrity Constraint violation, then 
variable ``v1`` gets ``'c-err'``; if it succeeds but there is some warning, 
then variable ``v1`` gets ``'?????'``. But, regardless, play continues because 
all the handlers are ``CONTINUE`` handlers. So the second ``INSERT`` statement 
will put in one of the values ``'Ovflw'``, ``'c-err'``, ``'?????'`` or 
``'Okay!'`` (``'Okay!'`` is the default value for ``v1`` so this is what goes 
in if the result of the first ``INSERT`` is success with no warnings). 

What if exception ``'42000'`` happens? That would be an "unhandled exception" 
since we did not define a handler for exception ``'42000'``. The result would 
be that the second ``INSERT`` is not attempted -- the whole compound statement 
fails. 

The following chart compares the exception-handling features of embedded SQL,
the CLI and the PSM.

::

                                    EMBEDDED SQL       CLI   PSM
    method of declaration           EXEC SQL WHENEVER  none  handler-declaration
    what happens                    GOTO               N/A   any SQL statement
    handles SQLNOTFOUND?            yes                N/A   yes
    handles SQLERROR?               yes                N/A   yes
    handles SQLWARNING?             yes                N/A   yes
    handles specific status codes?  no                 N/A   yes

Among the SQL statements that a handler can execute are two new special ones:
the ``SIGNAL`` statement and the ``RESIGNAL`` statement. These SQL statements 
affect the diagnostics area.

Labels
______

We're still not done with the ``BEGIN ... END`` statement. The final form of a
compound statement adds two more optional clauses: a beginning label and an
end label. The required syntax for a compound statement is:

::

    [ <beginning_label>: ]
    BEGIN [ [ NOT ] ATOMIC ]
      [ <variable | condition declaration>; ... ]
      [ DECLARE CURSOR statement; ... ]
      [ <handler declaration>; ...]
      [ <SQL statement>; ... ]
    END [ <end_label> ]
    
    <beginning_label> ::= <identifier>
    
    <end_label> ::= <identifier>

If you add labels to your compound statement, they should be equivalent (if
both are specified). Labels are useful as referents for various control
statements, which we will discuss later. Here's an example:

::

  full_blown_example:                      /* beginning_label */
  BEGIN ATOMIC                             /* compound statement is atomic */
    DECLARE v1 INTEGER DEFAULT 0;          /* variable declaration */
    DECLARE c1 CONDITION FOR '01000';      /* condition declaration */
    DECLARE CONTINUE HANDLER FOR SQLERROR  /* handler declaration */
      SET v1 = 1;                          /* assignment statement */
    INSERT INTO Table_1 VALUES (0);        /* statement */
    INSERT INTO Table_2 VALUES (v1);       /* statement */
  END full_blown_example                   /* end_label */

This is our final version of ``BEGIN .. END``. It looks quite imposing. That's
because MOST SYNTACTIC ITEMS ARE LOCAL TO THE COMPOUND STATEMENT. Therefore
everything is within the compound statement and, by contrast, the Module
definition is trivial.

*SIGNAL Statement*
------------------

The ``SIGNAL`` statement is used to clear the diagnostics area. The required 
syntax for the ``SIGNAL`` statement is:

::

    SIGNAL <condition name or sqlstate value>
       SET <signal information item list>
       
       <signal information item list> ::=
       <signal information item> [ {,<signal information item>}... ]
       
          <signal information item> ::=
          <condition information item name> = <simple value specification>

The ``SIGNAL`` statement clears every record in the diagnostics area. The end
result is a record containing the passed condition name or sqlstate value. If
you include the optional ``SET`` clause, your DBMS effectively executes:

::

   RESIGNAL <signal information item list>;

**Note:** You'll find the list of <condition information item name>s in our 
chapter on embedded SQL -- see the ``GET DIAGNOSTICS`` statement.

*RESIGNAL Statement*
--------------------

The ``RESIGNAL`` statement is used to pass conditions on to another handler. The
required syntax for the ``RESIGNAL`` statement is:

::

    RESIGNAL [ <condition name or sqlstate value> ]
       SET <signal information item list>

The ``RESIGNAL`` statement passes the given exception "up the line" to the next
appropriate handler (since compound statements may be embedded in compound
statements, this next appropriate handler will usually be in some outside
context). The current diagnostics area remains unchanged, but -- if the
optional [<condition name or sqlstate value>] clause is specified -- there
will be one more diagnostics record, containing this new value. If you include
the optional ``SET`` clause, the <condition information item name> field in the
first condition area in the diagnostics area is changed to the value indicated.

Program Control
_______________

Essential SQL has almost nothing that can control the program flow (except for
the ``CALL`` and ``RETURN`` statements which are associated with SQL routines). 
By contrast, a DBMS with PSM support will allow eight control statements. Of
these, seven are similar to statements which appear in other languages. The
eighth, ``FOR``, depends on Objects which are unique to the SQL environment.
Here's a list of these statements:

::

    CASE -- Switch depending on condition.
    IF -- If (condition) do.
    ITERATE -- Restart loop.
    LOOP -- Do statement(s) repeatedly.
    LEAVE -- Break out of a loop or block.
    WHILE -- Repeat statement(s) as long as condition is true.
    REPEAT -- Repeat statement(s) until condition is true.
    FOR -- Cursor-based FETCH loop.

*CASE Statement*
----------------

The ``CASE`` statement is useful for switching between possible execution paths.
There are two forms -- one contains search conditions, the other contains
value expressions. The required syntax for the ``CASE`` statement is:

::

    searched CASE statement ::=
    CASE
      WHEN <search condition> THEN <statement>(s)
      [ WHEN <search condition> THEN <statement>(s) ... ]
      [ ELSE <statement>(s) ]
    END CASE
    
    simple CASE statement ::=
    CASE <case value>
       WHEN <when value> THEN <statement>(s)
       [ WHEN <when value> THEN <statement>(s) ... ]
       [ ELSE <statement>(s) ]
    END CASE

A "simple ``CASE`` statement" is merely a shorthand, and may be replaced by a 
"searched ``CASE`` statement" which has the form: "``CASE WHEN`` <when value> = 
<case value> ...". Thus, the following examples, showing a searched ``CASE`` 
statement on the left and a simple ``CASE`` statement on the right, are exactly 
equivalent: 

::

   CASE                                CASE parameter_value
     WHEN parameter_value = 15           WHEN 15
      THEN INSERT INTO t VALUES (15);     THEN INSERT INTO t VALUES (15);
     WHEN parameter_value = 17           WHEN 17
      THEN INSERT INTO t VALUES (17);     THEN INSERT INTO t VALUES (17);
     ELSE INSERT INTO t VALUES (0);      ELSE INSERT INTO t VALUES (0);
   END CASE                            END CASE

When executing a ``CASE`` statement, the DBMS goes through the ``WHEN`` clauses 
from top to bottom, looking for a ``TRUE`` condition. If it finds one, it 
executes the statement(s) after ``THEN``, and the ``CASE`` terminates. If it 
finds none, it executes the statements(s) after ``ELSE`` -- or, if there is no 
``ELSE``, returns this ``SQLSTATE error: 20000 "case not found for case 
statement"``. For the above example, then, if the value of ``parameter_value`` 
is ``5``, then the DBMS will execute this SQL statement: 

::

   INSERT INTO t VALUES (0);

.. CAUTION:: 

   The syntax for the ``CASE`` statement is somewhat different from the syntax 
   for the SQL ``CASE`` expression (see our chapter on Simple Search 
   Conditions). In particular, the ``CASE`` statement has no equivalent for the 
   ``ELSE NULL`` clause, and the terminator is ``END CASE`` rather than 
   ``END``. 

*IF Statement*
--------------

The ``IF`` statement is useful for simple "if (x) then (do this)" situations. 
The required syntax for the ``IF`` statement is:

::

    IF <search condition> THEN <SQL statement>(s)
       ELSEIF <search condition> THEN <SQL statement>(s)
       ELSE <SQL statement>(s)
    END IF

Here's an example:

::

  IF
   5=5 THEN UPDATE Table_1 SET column_1 = column_1 + 1;
  END IF

In this example, the search condition is ``TRUE``, so the ``UPDATE`` statement 
will be executed. If the search condition had been ``FALSE`` or ``UNKNOWN``, 
then the ``UPDATE`` statement would not have been executed. 

*LOOP Statement*
----------------

The ``LOOP`` statement is useful for repeated execution of SQL statements. The
required syntax for the ``LOOP`` statement is:

::

    [ <beginning_label>: ]
    LOOP
       <SQL statement>(s)
    END LOOP [ <end_label> ]

The SQL statements between ``LOOP`` and ``END LOOP`` are repeated until the loop
finishes. The <beginning_label> and the <end_label> must be equivalent, if you
use them both. Here's an example:

::

   LOOP
      SET x = x + 1;
   END LOOP

This example shows an infinite loop. The usual way to exit from a loop is with
the ``LEAVE`` statement.

*LEAVE Statement*
-----------------

The ``LEAVE`` statement is useful for exiting a block or for exiting a loop. The
required syntax for the ``LEAVE`` statement is:

::

    LEAVE <statement_label>

Here's an example:

::

   beginning_label:
   LOOP
     SET x = x + 1;
     IF x > 1000 THEN LEAVE beginning_label; END IF;
   END LOOP beginning_label

In this example, the loop will be exited once the value of ``x`` passes 1000.

*WHILE Statement*
-----------------

The ``WHILE`` statement is useful for repeated execution of SQL statements, with
a built-in equivalent to the ``LEAVE`` statement. The required syntax for the 
``WHILE`` statement is:

::

    [ <beginning_label>: ]
    WHILE <search condition> DO
       <SQL statement>(s)
    END WHILE [ <end_label> ]

As long as the <search condition> is ``TRUE``, the SQL statements between 
``WHILE`` and ``END WHILE`` are repeatedly executed. The <beginning_label> and 
the <end_label> must be equivalent, if you use them both. Here's an example: 

::

   WHILE x <= 1000 DO
      SET x = x + 1;
   END WHILE

This example will loop, incrementing ``x``, until "``x <= 1000``" is either 
``FALSE`` or ``UNKNOWN``. If the <search condition> is ``FALSE`` or ``UNKNOWN`` 
when the loop begins, then nothing happens. 

*REPEAT Statement*
------------------

The ``REPEAT`` statement is much like the ``WHILE`` statement, except that the
condition is tested after the execution of the SQL statement(s). The required
syntax for the ``REPEAT`` statement is:

::

    [ <beginning_label>: ]
    REPEAT
       <SQL statement>(s) UNTIL <search condition>
    END REPEAT [ <end_label> ]

As long as the <search condition> is ``FALSE`` or ``UNKNOWN``, the SQL 
statements between ``REPEAT`` and ``END REPEAT`` are repeatedly executed. The 
<beginning_label> and the <end_label> must be equivalent, if you use them both. 
Here's an example: 

::

   REPEAT
      DELETE FROM Table_1 WHERE column_1 = x;
      SET x = x + 1;
      UNTIL x > 5
   END REPEAT

In this example, the ``UPDATE`` statement will be repeated until ``x`` is 
greater than 5 -- that is, the loop will repeat until after theIf a sensitive 
or asensitive holdable-Cursor is held open for a subsequent transaction, then 
whether any significant changes made to SQL-data (by this or any subsequent 
transaction in which the Cursor is held open) will be visible through that 
Cursor in the subsequent transaction is non-standard because the SQL Standard 
requires implementors to define how they will handle this situation. 

Whether a DBMS is able to disallow significant changes that would not be 
visible through a currently open Cursor is non-standard because the SQL 
Standard requires implementors to define their actions in such situations. 

The extent to which a DBMS may disallow independent changes that are not 
significant is non-standard because the SQL Standard requires implementors to 
define their actions in such situations. 

The status of any open Cursors in any SQL-client Module associated with the 
current transaction that were opened by that transaction before the 
establishment of a savepoint to which a ``ROLLBACK`` is executed is 
non-standard because the SQL Standard requires implementors to define their 
actions in such situations.

*Diagnostics*
-------------

The actual length of variable-length character items in the diagnostics area 
has to be at least 128 octets but is otherwise non-standard because the SQL 
Standard requires implementors to define the actual length. 

The character string value set for the diagnostic area's ``CLASS_ORIGIN`` and 
``SUBCLASS_ORIGIN`` fields may not be ``'ISO 9075'`` but is otherwise 
non-standard because the SQL Standard requires implementors to define their own 
values for any non-standard errors. 

The character string value set for the diagnostic area's ``MESSAGE_TEXT`` field 
is non-standard because the SQL Standard requires implementors to define their 
own values for this field. 

Any negative values set for the diagnostic area's ``COMMAND_FUNCTION_CODE`` 
field indicate implementation-defined SQL-statements and are thus non-standard 
because the SQL Standard requires implementors to define their own values for 
this field if they support any non-standard SQL statements. 

The method of flagging nonconforming SQL language or processing of conforming 
SQL language is implementation-defined, as is the list of additional <keyword>s 
that may be required by the DBMS. 

The full set of known functional dependencies is non-standard because the SQL 
Standard allows implementors to define additional functional dependencies if 
they choose. 

Implementation-Dependent Features
=================================

The SQL Standard requires a SQL DBMS to define how it will handle each of these 
features. The decision does not have to be documented. 

If more than one condition could have occurred when executing an SQL statement, 
it is implementation-dependent whether the DBMS will make diagnostic 
information pertaining to more than one condition available. 

The treatment of language that does not conform to the SQL Standard is 
implementation-dependent. 

If evaluation of the inessential parts of an expression or search condition 
would cause an exception condition to be raised, it is implementation-dependent 
whether or not that condition is raised. 

The actual size of the diagnostics area is implementation-dependent if you 
don't specify the size yourself. 

If ``DECLARE CURSOR`` does not include an ``ORDER BY`` clause, or includes an 
``ORDER BY`` clause that doesn't specify the order of the rows completely, then 
the rows of the result Table have an order that is defined only to the extent 
that the ``ORDER BY`` clause specifies and is otherwise 
implementation-dependent. 

The effect on the position and state of an open Cursor when an error occurs 
during the execution of an SQL statement that identifies the Cursor is 
implementation-dependent. 

If an asensitive Cursor is open and a change is made to SQL-data from within 
the same transaction other than through that Cursor, then whether that change 
will be visible through that Cursor before it is closed is 
implementation-dependent. 

The mapping of <AuthorizationID>s to operating system users is 
implementation-dependent. 

When an SQL-session is initiated, the current <authorization identifier> for 
the SQL-session is determined in an implementation-dependent manner, unless the 
session is initiated using a <connect statement>. 

A unique implementation-dependent SQL-session identifier is associated with 
each SQL-session. 

The SQL-client <Module name> of the SQL-client Module that is effectively 
materialized on an SQL-server is implementation-dependent. 

Diagnostic information is passed to the diagnostics area in an application in 
an implementation-dependent manner. 

The effect on diagnostic information of incompatibilities between the character 
repertoires supported by the SQL-client and SQL-server environments is 
implementation-dependent. 

The time of evaluation of the ``CURRENT_DATE``, ``CURRENT_TIME`` and 
``CURRENT_TIMESTAMP`` functions during the execution of an SQL statement is 
implementation-dependent. 

The start datetime used for converting intervals to scalars for subtraction 
purposes is implementation-dependent. 

The names of the Columns of a <row value constructor> that specifies a <row 
value constructor list> are implementation-dependent. 

When a Column is not named by an ``AS`` clause and is not derived from a single 
Column reference, then the name of the Column is implementation-dependent. 

If a <simple Table> is neither a <query specification> nor an <explicit Table>, 
then the name of each Column of the <simple Table> is implementation-dependent. 

If a <non-join query term> is not a <non-join query primary> and the <Column 
name> of the corresponding Columns of both Tables participating in the 
<non-join query term> are not the same, then the result Column has an 
implementation-dependent <Column name>. 

If a <non-join query expression> is not a <non-join query term> and the <Column 
name> of the corresponding Columns of both Tables participating in the 
<non-join query expression> are not the same, then the result Column has an 
implementation-dependent <Column name>. 

When the operations ``MAX``, ``MIN``, ``DISTINCT``, and references to a 
grouping Column refer to a variable-length character string or a 
variable-length bit string, the specific value selected from the set of equal 
values is implementation-dependent. 

The specific Character set chosen for the result of an aggregation is 
implementation-dependent, but must be the Character set of one of the <data 
type>s being aggregated. 

The <Constraint name> of a Constraint that does not specify a <Constraint name> 
is implementation-dependent. 

The specific value to use for cascading foreign keys among various values that 
are not distinct is implementation-dependent. 

The Collation of characters for which a Collation is not otherwise specified is 
implementation-dependent. 

If an error occurs during assignment of a value to a target during the 
execution of a singleton ``SELECT``, the values of targets other than status 
parameters are implementation-dependent. 

If the cardinality of a singleton ``SELECT`` is greater than one, it is 
implementation-dependent whether or not values are assigned to the 
``SELECT``\'s targets. 

For Cursor operations, if an exception condition occurs during the assignment 
of a value to a target, the values of all targets are implementation-dependent 
and the Cursor remains positioned on the current row. 

It is implementation-dependent whether a Cursor remains positioned on the 
current row when an exception condition is raised during the derivation of any 
derived Column. 

If <number of conditions> for the diagnostics area is not specified in a ``SET 
TRANSACTION`` statement, then an implementation-dependent value, not less than 
one, is the default. 

The value of the diagnostic area's ``ROW_COUNT`` following the execution of an 
SQL-statement that does not directly result in the execution of a <delete 
statement: searched>, an <insert statement> or an <update statement: searched> 
is implementation-dependent. 
