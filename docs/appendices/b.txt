.. highlight:: text

==========================
Appendix B -- SQL Taxonomy
==========================

For easy reference, this appendix gathers together all of our notes on what to
avoid if you want to restrict your code to Core SQL. It also includes the SQL
Taxonomy tables from the SQL Standard -- these list all of the features
required for full SQL3 support, noting those which are required for Core SQL
support.

.. rubric:: Table of Contents

.. contents::
    :local:

Core SQL Notes
--------------

* If you want to restrict your code to Core SQL, don't use bracketed
  comments.

* If you want to restrict your code to Core SQL, make sure your <regular
  identifier>s and your <delimited identifier>s are no more than 18 characters
  long.

* If you want to restrict your code to Core SQL, do not use either binary or
  hexadecimal <bit string literal>s.

* If you want to restrict your code to Core SQL, don't define any ``BIT`` or ``BIT
  VARYING`` <data type>s.

* If you want to restrict your code to Core SQL, don't use the concatenation
  operator, ``SUBSTRING`` or ``POSITION`` with bit strings.

* If you want to restrict your code to Core SQL, don't use ``BLOB``\s in
  comparisons.

* If you want to restrict your code to Core SQL, don't use the concatenation
  operator, ``SUBSTRING`` or the ``[NOT LIKE]`` predicate with ``BLOB``\s.

* If you want to restrict your code to Core SQL, don't add a Character set
  specification to <character string literal>s, don't add a ``COLLATE`` clause 
  to <character string literal>s and don't split long <character string 
  literal>s into smaller strings.

* If you want to restrict your code to Core SQL, don't use <national
  character string literal>s.

* If you want to restrict your code to Core SQL, don't use the ``CHARACTER SET``
  clause or the ``COLLATE`` clause for ``CHAR`` or ``VARCHAR`` or ``CLOB`` 
  <data type> specifications.

* If you want to restrict your code to Core SQL, don't use the ``NCHAR`` or 
  ``NCHAR VARYING`` or ``NCLOB`` <data type>s.

* If you want to restrict your code to Core SQL, don't use ``CLOB``\s or 
  ``NCLOB``\s in comparisons.

* If you want to restrict your code to Core SQL, don't use the concatenation
  operator with ``CLOB``\s or ``NCLOB``\s and don't use the ``COLLATE`` clause 
  to force an ``EXPLICIT`` Collation for any character string concatenation.

* If you want to restrict your code to Core SQL, don't use ``SUBSTRING`` with 
  ``NCLOB``\s and don't use the ``COLLATE`` clause to force an ``EXPLICIT`` 
  Collation for any ``SUBSTRING`` operation.

* If you want to restrict your code to Core SQL, don't use ``OVERLAY`` with
  character strings.

* If you want to restrict your code to Core SQL, don't use ``TRIM`` with 
  ``NCLOB``\s and don't use the ``COLLATE`` clause to force an ``EXPLICIT`` 
  Collation for any ``TRIM`` operation.

* If you want to restrict your code to Core SQL, don't use the ``COLLATE`` 
  clause to force an ``EXPLICIT`` Collation for any ``UPPER`` or ``LOWER`` 
  operation.

* If you want to restrict your code to Core SQL, don't use ``TRANSLATE``.

* If you want to restrict your code to Core SQL, don't use ``CONVERT``.

* If you want to restrict your code to Core SQL, don't use the <regular
  expression substring function> form of ``SUBSTRING``.

* If you want to restrict your code to Core SQL, don't use ``POSITION`` with
  character strings.

* If you want to restrict your code to Core SQL, don't use ``BIT_LENGTH``,
  ``CHAR_LENGTH`` or ``OCTET_LENGTH`` with ``NCLOB``\s.

* If you want to restrict your code to Core SQL, don't use the ``[NOT] LIKE``
  predicate with ``CLOB``\s or ``NCLOB``\s and, when you do use ``[NOT LIKE]``, 
  make sure your ``character_string_argument`` is a <Column reference> and that 
  your ``pattern`` and your ``escape_character`` are both 
  <value specification>s.

* If you want to restrict your code to Core SQL, don't use the ``[NOT] SIMILAR``
  predicate.

* If you want to restrict your code to Core SQL, don't explicitly define the
  Character set that any character string belongs to -- always allow it to
  belong to the default Character set.

* If you want to restrict your code to Core SQL, don't use <time zone
  interval>s.

* If you want to restrict your code to Core SQL, don't add a fractional
  seconds precision or a <time zone interval> to your time values.

* If you want to restrict your code to Core SQL, don't add a fractional
  seconds precision greater than 6 digits or a <time zone interval> to your
  timestamp values.

* If you want to restrict your code to Core SQL, don't define your ``TIME`` 
  <data type>s with a fractional seconds precision and don't add the optional 
  noise words ``WITHOUT TIME ZONE``: use only ``TIME``, never ``TIME(x) WITHOUT 
  TIME ZONE``.

* If you want to restrict your code to Core SQL, don't use ``TIME WITH TIME
  ZONE`` <data type>s.

* If you want to restrict your code to Core SQL, don't define your T``IMESTAMP``
  <data type>s with a fractional seconds precision other than 0 or 6 and don't
  add the optional noise words ``WITHOUT TIME ZONE``: use only ``TIMESTAMP``,
  ``TIMESTAMP(0)`` or ``TIMESTAMP(6)``, never ``TIMESTAMP(x) WITHOUT TIME ZONE``.

* If you want to restrict your code to Core SQL, don't use ``TIMESTAMP WITH
  TIME ZONE`` <data type>s.

* If you want to restrict your code to Core SQL, don't use <interval
  literal>s.

* If you want to restrict your code to Core SQL, don't use the INTERVAL <data
  type>.

* If you want to restrict your code to Core SQL, don't add or subtract
  datetime expressions, don't add the optional ``AT LOCAL/AT TIME ZONE`` clause 
  to any time or timestamp value and don't use interval expressions at all.

* If you want to restrict your code to Core SQL, don't use ``CURRENT_TIME`` or
  ``CURRENT_TIMESTAMP``, don't specify a fractional seconds precision for 
  ``LOCALTIME`` and don't specify a fractional seconds precision for 
  ``LOCALTIMESTAMP`` other than zero or 6.

* If you want to restrict your code to Core SQL, don't use ``EXTRACT``.

* If you want to restrict your code to Core SQL, don't use ``ABS`` with an
  interval argument.

* If you want to restrict your code to Core SQL, don't use the ``OVERLAPS``
  predicate.

* If you want to restrict your code to Core SQL, don't use <boolean
  literal>s.

* If you want to restrict your code to Core SQL, don't define any ``BOOLEAN``
  <data type>s.

* If you want to restrict your code to Core SQL, don't use the optional truth
  value Boolean test (i.e.: don't use the constructs "boolean_argument" ``IS 
  TRUE``, "boolean_argument" ``IS FALSE`` or "boolean_argument" ``IS UNKNOWN``) 
  and don't use "boolean_argument" unless it's an SQL predicate or it's 
  enclosed in parentheses.

* If you want to restrict your code to Core SQL, don't define any ``ARRAY`` 
  <data type>s and don't use any of SQL's array syntax.

* If you want to restrict your code to Core SQL, don't use ``CONCATENATE``.

* If you want to restrict your code to Core SQL, don't use ``CARDINALITY``.

* If you want to restrict your code to Core SQL, don't use the ``ROW`` <data
  type> or <row reference>s and <Field reference>s and, when using a <row value
  constructor>, don't use ``ARRAY[]`` or ``ARRAY??(??)`` as an 
  "element_expression", don't construct a row with more than one Field, don't 
  use the ``ROW`` <keyword> in front of your element_expression and don't use a 
  subquery to construct your row.

* If you want to restrict your code to Core SQL, don't use the ``REF`` <data
  type>.

* If you want to restrict your code to Core SQL, don't use ``DEREF``.

* If you want to restrict your code to Core SQL, don't use ``UDT``\s, methods 
  or any of SQL's <reference type> or ``UDT`` syntax.

* If you want to restrict your code to Core SQL, don't use <Domain name> as a
  ``CAST`` target: ``CAST`` only to a <data type>.

* If you want to restrict your code to Core SQL, don't use ``CAST`` to convert
  any ``BLOB`` value to another <data type>.

* If you want to restrict your code to Core SQL, don't use ``CAST`` to convert
  any ``CLOB`` or ``NCLOB`` values to another <data type>.

* If you want to restrict your code to Core SQL, don't use this expression:
  ``NULL IS NULL`` or this expression: ``NULL IS NOT NULL``.

* If you want to restrict your code to Core SQL, don't use the ``CREATE ROLE``
  statement.

* If you want to restrict your code to Core SQL, don't specify the ``UNDER``
  Privilege, don't specify the ``SELECT`` Privilege as a Column Privilege (that 
  is, with a <Column name> list) and don't specify the ``INSERT`` Privilege as 
  a Column Privilege.

* If you want to restrict your code to Core SQL, don't use the ``FROM`` 
  <grantor> clause with the ``GRANT`` statement.

* If you want to restrict your code to Core SQL, don't use the <grant role
  statement> form of the ``GRANT`` statement and don't grant any grantable
  Privileges on your Objects to other users -- Core SQL only allows the owner of
  an Object to hold a grantable Privilege.

* If you want to restrict your code to Core SQL, don't use the <revoke role 
  statement> form of the ``REVOKE`` statement and don't use ``REVOKE ... 
  CASCADE`` or the ``GRANT OPTION FOR`` clause. Also, when revoking, make sure 
  that your current <AuthorizationID> is the owner of the Schema that owns the 
  Object you're revoking Privileges for. 

* If you want to restrict your code to Core SQL, don't use the ``DROP ROLE``
  statement.

* If you want to restrict your code to Core SQL, don't use ``CURRENT_USER``,
  ``SESSION_USER``, ``SYSTEM_USER`` or ``CURRENT_ROLE``.

* If you want to restrict your code to Core SQL, don't use explicit <Catalog
  name>s.

* If you want to restrict your code to Core SQL, do not reference
  
  ::
  
   INFORMATION_SCHEMA.ADMINISTRABLE_ROLE_AUTHORIZATIONS,
   INFORMATION_SCHEMA.APPLICABLE_ROLES, 
   INFORMATION_SCHEMA.ASSERTIONS,
   INFORMATION_SCHEMA.COLLATIONS, 
   INFORMATION_SCHEMA.COLUMN_DOMAIN_USAGE,
   INFORMATION_SCHEMA.COLUMN_PRIVILEGES,
   INFORMATION_SCHEMA.COLUMN_USER_DEFINED_TYPE_USAGE,
   INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE,
   INFORMATION_SCHEMA.CONSTRAINT_TABLE_USAGE,
   INFORMATION_SCHEMA.DIRECT_SUPERTABLES, 
   INFORMATION_SCHEMA.DOMAINS,
   INFORMATION_SCHEMA.DOMAIN_CONSTRAINTS,
   INFORMATION_SCHEMA.DOMAIN_USER_DEFINED_TYPE_USAGE,
   INFORMATION_SCHEMA.ENABLED_ROLES, 
   INFORMATION_SCHEMA.KEY_COLUMN_USAGE,
   INFORMATION_SCHEMA.METHOD_SIGNATURES,
   INFORMATION_SCHEMA.METHOD_SIGNATURE_PARAMETERS,
   INFORMATION_SCHEMA.ROLE_COLUMN_GRANTS, 
   INFORMATION_SCHEMA.ROLE_ROUTINE_GRANTS,
   INFORMATION_SCHEMA.ROLE_TABLE_GRANTS, 
   INFORMATION_SCHEMA.ROLE_USAGE_GRANTS,
   INFORMATION_SCHEMA.ROLE_USER_DEFINED_TYPE_GRANTS,
   INFORMATION_SCHEMA.ROUTINE_COLUMN_USAGE,
   INFORMATION_SCHEMA.ROUTINE_TABLE_USAGE, 
   INFORMATION_SCHEMA.SQL_FEATURES,
   INFORMATION_SCHEMA.SQL_IMPLEMENTATION_INFO, 
   INFORMATION_SCHEMA.SQL_SIZING,
   INFORMATION_SCHEMA.SQL_SIZING_PROFILES, 
   INFORMATION_SCHEMA.TABLE_PRIVILEGES,
   INFORMATION_SCHEMA.TRANSFORMS, 
   INFORMATION_SCHEMA.TRANSLATIONS,
   INFORMATION_SCHEMA.TRIGGER_COLUMN_USAGE,
   INFORMATION_SCHEMA.TRIGGER_TABLE_USAGE, 
   INFORMATION_SCHEMA.USAGE_PRIVILEGES,
   INFORMATION_SCHEMA.USER_DEFINED_TYPE_PRIVILEGES,
   INFORMATION_SCHEMA.USER_DEFINED_TYPES, 
   INFORMATION_SCHEMA.VIEW_COLUMN_USAGE or
   INFORMATION_SCHEMA.VIEW_TABLE_USAGE.

* If you want to restrict your code to Core SQL, don't use a ``DEFAULT 
  CHARACTER SET`` clause or a ``PATH`` clause in your ``CREATE SCHEMA`` 
  statements and don't include any of the following in your <Schema element 
  list>: ``CREATE ASSERTION`` statements, ``CREATE CHARACTER SET`` statements, 
  ``CREATE COLLATION`` statements, ``CREATE DOMAIN`` statements, ``CREATE 
  TRANSLATION`` statements, ``CREATE TYPE`` statements, ``CREATE ROLE`` 
  statements or ``GRANT`` statements to Roles. 

* If you want to restrict your code to Core SQL, don't use the ``DROP SCHEMA``
  statement.

* If you want to restrict your code to Core SQL, don't create any temporary
  Base tables, don't use a ``LIKE`` clause as a <table element>, don't use an 
  ``OF`` clause as a <table element> and don't add a <column scope clause> to 
  any ``CREATE TABLE`` statement.

* If you want to restrict your code to Core SQL, don't add a ``COLLATE`` clause
  to your <Column definition>s, don't base your Columns on Domains, don't name
  your <Column Constraint>s and don't define a <Column Constraint> with a
  <referential triggered action>.

* If you want to restrict your code to Core SQL, don't use ``DEFAULT
  CURRENT_PATH`` when defining a <default clause>.

* If you want to restrict your code to Core SQL, don't use ``ALTER TABLE`` to
  drop a Column from a Table, to change a <Column definition> using any of the
  available options, to add a Constraint to a Table or to drop a Constraint from
  a Table.

* If you want to restrict your code to Core SQL, don't use the ``CASCADE`` drop
  behaviour for your ``DROP TABLE`` statements.

* If you want to restrict your code to Core SQL, don't define any ``RECURSIVE`` 
  Views, don't use the ``EXCEPT``, ``INTERSECT`` or ``CORRESPONDING`` operators 
  in your View queries and don't use the optional ``CASCADED`` or ``LOCAL`` 
  levels specification in your check clauses -- always define Views only with 
  ``WITH CHECK OPTION`` alone. 

* If you want to restrict your code to Core SQL, don't use the ``CASCADE`` drop
  behaviour for your ``DROP VIEW`` statements.

* If you want to restrict your code to Core SQL, don't use the ``DECLARE LOCAL 
  TEMPORARY TABLE`` statement.

* If you want to restrict your code to Core SQL, don't use the ``CREATE DOMAIN``
  statement.

* If you want to restrict your code to Core SQL, don't use the ``ALTER DOMAIN``
  statement.

* If you want to restrict your code to Core SQL, don't use the ``DROP DOMAIN``
  statement.

* If you want to restrict your code to Core SQL, don't name your Constraints
  and don't add a <constraint attributes> clause to your Constraint definitions.
  (This means you'll be defining all Constraints as ``NOT DEFERRABLE 
  INITIALLY IMMEDIATE``.)

* If you want to restrict your code to Core SQL, don't use the
  ``UNIQUE(VALUE)`` form to define a ``UNIQUE`` Constraint and don't add a 
  ``NOT NULL`` Constraint to any Column that is part of a unique key for a 
  ``UNIQUE`` Constraint.

* If you want to restrict your code to Core SQL, don't define your ``FOREIGN
  KEY`` Constraints with a ``MATCH`` clause, an ``ON UPDATE`` clause or an 
  ``ON DELETE`` clause.

* If you want to restrict your code to Core SQL, don't use a subquery in a 
  ``CHECK`` Constraint's search condition. Also, for Core SQL, the 
  ``REFERENCES`` Privilege isn't needed to create a ``CHECK`` Constraint. 

* If you want to restrict your code to Core SQL, don't use the ``CREATE
  ASSERTION`` statement.

* If you want to restrict your code to Core SQL, don't use the ``DROP 
  ASSERTION`` statement.

* If you want to restrict your code to Core SQL, don't use any <Character set
  name>s.

* If you want to restrict your code to Core SQL, don't use the ``CREATE
  CHARACTER SET`` statement.

* If you want to restrict your code to Core SQL, don't use the ``DROP 
  CHARACTER SET`` statement.

* If you want to restrict your code to Core SQL, don't use any <Collation
  name>s or <Form-of-use conversion name>s.

* If you want to restrict your code to Core SQL, don't use the ``CREATE
  COLLATION`` statement.

* If you want to restrict your code to Core SQL, don't use the ``DROP 
  COLLATION`` statement.

* If you want to restrict your code to Core SQL, don't use any <Translation
  name>s.

* If you want to restrict your code to Core SQL, don't use the ``CREATE
  TRANSLATION`` statement.

* If you want to restrict your code to Core SQL, don't use the ``DROP
  TRANSLATION`` statement.

* If you want to restrict your code to Core SQL, don't use the ``CREATE 
  TRIGGER`` statement.

* If you want to restrict your code to Core SQL, don't use the ``DROP 
  TRIGGER`` statement.

* If you want to restrict your code to Core SQL, don't use ``LOCATOR`` 
  indicators, ``DYNAMIC RESULT SETS`` clauses, ``TRANSFORM GROUP`` clauses or 
  duplicate <Routine name>s when defining an SQL-invoked routine and don't 
  define any SQL-invoked methods. 

* If you want to restrict your code to Core SQL, don't use the ``CASCADE`` drop
  behaviour for your ``DROP ROUTINE/FUNCTION/PROCEDURE`` statements.

* If you want to restrict your code to Core SQL, don't use an <element
  reference> or ``CURRENT_PATH`` to specify a value.

* If you want to restrict your code to Core SQL, don't use a <value
  expression> that evaluates to a Boolean value, an array, an interval or a 
  ``REF`` value, don't use a <subtype treatment> to specify a value and don't 
  use the ``COLLATE`` clause to force a collating sequence for any value.

* If you want to restrict your code to Core SQL, don't use a <query name> to
  make up a <Table reference> and don't use the <keyword> ``ONLY`` to make up a
  <Table reference> that refers to a typed Table.

* If you want to restrict your code to Core SQL, don't use the <distinct
  predicate>.

* If you want to restrict your code to Core SQL, don't use ``BLOB``\s, 
  ``CLOB``\s or ``NCLOB``\s in a ``CASE`` expression.

* If you want to restrict your code to Core SQL, don't use ``CROSS JOIN``, don't
  use ``UNION JOIN``, don't use ``NATURAL`` for any type of join and don't use 
  ``FULL [OUTER] JOIN``.

* If you want to restrict your code to Core SQL, make sure that all
  ``scalar_expressions`` in an <in value list> are either <literal>s, references
  to a host variables or SQL parameters, <Field reference>s or the ``USER``
  function.

* If you want to restrict your code to Core SQL, don't use the <unique
  predicate>.

* If you want to restrict your code to Core SQL, don't use the <match
  predicate>.

* If you want to restrict your code to Core SQL, don't use the <quantified
  predicate>.

* If you want to restrict your code to Core SQL, don't use ``TABLE`` <Table
  name>.

* If you want to restrict your code to Core SQL, don't use a Table
  constructor that involves a Table expression, don't use a Table constructor
  anywhere but in an ``INSERT`` statement and make all your Table constructors
  contain exactly one row.

* If you want to restrict your code to Core SQL, don't use ``WITH [RECURSIVE]``
  in a <query expression>, the ``INTERSECT`` set operator, a ``CORRESPONDING`` 
  clause with any set operator or any set operator with an explicit 
  ``DISTINCT``.

* If you want to restrict your code to Core SQL, don't use ``ROLLUP`` or 
  ``CUBE``, and don't add a ``COLLATE`` clause to any grouping Column reference.

* If you want to restrict your code to Core SQL, don't use the set functions 
  ``EVERY``, ``ANY``, ``SOME`` or ``GROUPING``, don't use a set function unless 
  it operates only on a <Column reference> that refers to a Column belonging to 
  a Table named in the ``FROM`` clause, and when counting, always use 
  ``COUNT(*)``: don't use ``COUNT(Column)`` or ``COUNT(ALL Column)`` at all. 

* If you want to restrict your code to Core SQL, don't use a <query expression> 
  with ``EXCEPT``, ``INTERSECT`` or ``CORRESPONDING`` in an ``INSERT`` 
  statement, don't use a <query expression> that names an underlying Table of 
  your target Table in an ``INSERT`` statement, don't use the <query 
  expression> ``TABLE`` <Table name> in an ``INSERT`` statement, if you use the 
  <query expression ``VALUES`` (value commalist) in an ``INSERT`` statement, 
  make sure it constructs only one new row, don't use the ``DEFAULT VALUES`` 
  form of the ``INSERT`` statement and make sure all your ``INSERT`` <Table 
  reference>s are actually <Table name>s, with no <Correlation name>s or 
  <derived Column list>s. 

* If you want to restrict your code to Core SQL, don't use a <search condition> 
  that names an underlying Table of your target Table in an ``UPDATE`` 
  statement and make sure all your ``UPDATE`` <Table reference>s are actually 
  <Table name>s, with no <Correlation name>s or <derived Column list>s. 

* If you want to restrict your code to Core SQL, don't use a <search condition> 
  that names an underlying Table of your target Table in a ``DELETE`` statement 
  and make sure all your ``DELETE`` <Table reference>s are actually <Table 
  name>s, with no <Correlation name>s or <derived Column list>s. 

* If you want to restrict your code to Core SQL, don't use ``AND CHAIN`` or 
  ``AND NO CHAIN`` with ``COMMIT``.

* If you want to restrict your code to Core SQL, don't use ``AND CHAIN``, ``AND 
  NO CHAIN`` or ``TO SAVEPOINT`` with ``ROLLBACK``.

* If you want to restrict your code to Core SQL, don't use the ``SAVEPOINT`` 
  statement.

* If you want to restrict your code to Core SQL, don't use the ``RELEASE 
  SAVEPOINT`` statement.

* If you want to restrict your code to Core SQL, don't use ``SET LOCAL
  TRANSACTION`` and don't set any transaction's isolation level to anything but
  ``SERIALIZABLE``.

* If you want to restrict your code to Core SQL, don't use the ``START
  TRANSACTION`` statement.

* If you want to restrict your code to Core SQL, don't use the ``CONNECT``
  statement.

* If you want to restrict your code to Core SQL, don't use the ``SET 
  CONNECTION`` statement.

* If you want to restrict your code to Core SQL, don't use the ``DISCONNECT``
  statement.

* If you want to restrict your code to Core SQL, don't use the ``SET SESSION
  CHARACTERISTICS`` statement.

* If you want to restrict your code to Core SQL, don't use the ``SET SESSION
  AUTHORIZATION`` statement.

* If you want to restrict your code to Core SQL, don't use the ``SET ROLE``
  statement.

* If you want to restrict your code to Core SQL, don't use the ``SET TIME ZONE``
  statement.

Taxonomy Tables
----------------

In the following tables:

* The first column, "Feature ID", gives the SQL Standard's identification 
  for each feature and subfeature. The Feature ID value consists of either a 
  letter and three digits or a letter, three digits, a hyphen and one or two 
  additional digits. Feature ID values without a hyphen identify complete 
  features. Feature ID values containing a hyphen and additional digits 
  identify subfeatures that help to define a complete feature. 

* The second column, "Feature Description", gives a brief description of 
  the feature or subfeature. 

* The third column, "Core SQL?", shows the SQL Standard's definition of 
  the minimal conformance requirement, called "Core SQL". Features that are 
  included in the definition of Core SQL contain a "YES" in this column (their 
  subfeatures contain "(yes)" for consistency). Features and subfeatures that 
  are not part of Core SQL contain a "No" in this column. 

Table Tax_1: SQL/Foundation Feature Taxonomy
............................................

::

    FEATURE  FEATURE                                                         CORE
    ID       DESCRIPTION                                                     SQL?
    E011     Numeric data types.                                             YES
    E011-1   The INTEGER and SMALLINT data types, integer literals, integer  (yes)
             expressions, integer comparison and integer assignment.
    E011-2   The REAL, DOUBLE PRECISION and FLOAT data types,                (yes)
             approximate numeric literals, approximate numeric expressions,
             approximate numeric comparison and approximate numeric
             assignment.
    E011-3   The DECIMAL and NUMERIC data types, decimal & numeric literals, (yes)
             decimal & numeric expressions, decimal & numeric comparison
             and decimal & numeric assignment.
    E011-4   The +, -, * and / arithmetic operators.                         (yes)
    E011-5   The =, <>, >, >=, < and <= operators.                           (yes)
    E011-6   Implicit casting among the numeric data types.                  (yes)
    E021     Character data types.                                           YES
    E021-1   CHARACTER data type (including all its spellings.               (yes)
    E021-2   CHARACTER VARYING data type (including all its spellings.       (yes)
    E021-3   Character literals, character comparison and character          (yes)
             assignment.
    E021-4   The CHARACTER_LENGTH function.                                  (yes)
    E021-5   The OCTET_LENGTH function.                                      (yes)
    E021-6   The SUBSTRING function for use with CHARACTER and CHARACTER     (yes)
             VARYING data types.
    E021-7   <character value expression>s by use of the concatenation       (yes)
             operation on CHARACTER and CHARACTER VARYING data types.
    E021-8   The UPPER and LOWER functions.                                  (yes)
    E021-9   The TRIM function.                                              (yes)
    E021-10  Implicit casting among the character data types.                (yes)
    E031     Identifiers.                                                    YES
    E031-1   Delimited identifiers.                                          (yes)
    E031-2   Lower case identifiers.                                         (yes)
    E031-3   Trailing underscore.                                            (yes)
    E041     Basic schema definition.                                        YES
    E041-1   <schema definition> as a means of defining base tables and      (yes)
             views, together with the ability to grant permissions on those
             base tables and views.
    E041-2   <table definition> for persistent base tables.                  (yes)
    E041-3   <view definition>.                                              (yes)
    E041-4   WITH CHECK OPTION clause on <view definition>.                  (yes)
    E041-5   <grant statement>.                                              (yes)
    E041-6   Allow the optional keyword TABLE on a <grant statement>.        (yes)
    E051     Basic query specification.                                      YES
    E051-1   SELECT DISTINCT.                                                (yes)
    E051-2   GROUP BY clause supported.                                      (yes)
    E051-3   A GROUP BY clause need not contain all the non-aggregated       (yes)
             columns in the select list.
    E051-4   A GROUP BY clause can contain columns that are not in the       (yes)
             select list.
    E051-5   <select list> items can be renamed (optional "AS <column name>" (yes)
             in <select sublist>).
    E051-6   HAVING clause supported.                                        (yes)
    E051-7   Qualified * in select list (<select list> item of the form      (yes)
             "<table name>.*" or "<correlation name>.*").
    E051-8   <correlation names> can be specified in the FROM clause and can (yes)
             be used elsewhere in the <query specification> to distinguish
             among columns.
    E051-9   Support for the ability to rename the columns in the FROM       (yes)
             clause (that is "FROM <table name> [ [AS] <correlation name> ]
             [ <column name> {, <column name>}... ]").
    E051-10  Derived tables supported in the FROM clause.                    (yes)
    E051-11  Allow the optional keyword AS before a <correlation name>.      (yes)
    E061     Basic predicates and search conditions.                         YES
    E061-1   <comparison predicate>.                                         (yes)
    E061-2   <between predicate>.                                            (yes)
    E061-3   <in predicate>.                                                 (yes)
    E061-4   <like predicate>.                                               (yes)
    E061-5   <like escape clause>.                                           (yes)
    E061-6   <null predicate>.                                               (yes)
    E061-7   <quantified comparison predicate>.                              (yes)
    E061-8   <exists predicate>.                                             (yes)
    E061-9   Subqueries in <comparison predicate>.                           (yes)
    E061-10  Subqueries in <exists predicate>.                               (yes)
    E061-11  Subqueries in <in predicate>.                                   (yes)
    E061-12  Subqueries in <quantified predicate>.                           (yes)
    E061-13  Correlated subqueries (<correlation names> used in a sub-query  (yes)
             as correlated reference to a column in the outer query).
    E061-14  <search condition> (two or more predicates combined using the   (yes)
             AND, OR and NOT logical operators).
    E071     Basic query expressions.                                        YES
    E071-1   UNION DISTINCT table operator.                                  (yes)
    E071-2   UNION ALL table operator.                                       (yes)
    E071-3   EXCEPT DISTINCT table operator.                                 (yes)
    E071-4   EXCEPT ALL table operator.                                      (yes)
    E071-5   Columns combined via table operators need not have exactly the  (yes)
             same data type.
    E071-6   Support of table operators within a subquery.                   (yes)
    E081     Basic Privileges.                                               YES
    E081-1   SELECT privilege.                                               (yes)
    E081-2   DELETE privilege.                                               (yes)
    E081-3   INSERT privilege at the table level.                            (yes)
    E081-4   UPDATE privilege at the table level.                            (yes)
    E081-5   UPDATE privilege at the column level.                           (yes)
    E081-6   REFERENCES privilege at the table level.                        (yes)
    E081-7   REFERENCES privilege at the column level.                       (yes)
    E081-8   WITH GRANT OPTION.                                              (yes)
    E091     Set functions.                                                  YES
    E091-1   AVG.                                                            (yes)
    E091-2   COUNT.                                                          (yes)
    E091-3   MAX.                                                            (yes)
    E091-4   MIN.                                                            (yes)
    E091-5   SUM.                                                            (yes)
    E091-6   ALL quantifier.                                                 (yes)
    E091-7   DISTINCT quantifier.                                            (yes)
    E101     Basic data manipulation.                                        YES
    E101-1   <insert statement>.                                             (yes)
    E101-2   The VALUES clause in an <insert statement> used to insert       YES
             multiple rows with one invocation.
    E101-3   <update statement: searched>.                                   (yes)
    E101-4   <delete statement: searched>.                                   (yes)
    E111     <select statement: single row>.                                 YES
    E121     Basic cursor support.                                           YES
    E121-1   <declare cursor>.                                               (yes)
    E121-2   Columns in the <order by clause> need not also be specified in  (yes)
             the <select list>.
    E121-3   Value expressions in ORDER BY clause (that is, a <sort key>     (yes)
             element is not restricted to being either a <column name> or an
             <integer> that designates a column>).
    E121-4   <open statement>.                                               (yes)
    E121-5   <fetch statement>.                                              (yes)
    E121-6   <update statement: positioned>.                                 (yes)
    E121-7   <delete statement: positioned>.                                 (yes)
    E121-8   <close statement>.                                              (yes)
    E121-10  FETCH with implicit NEXT.                                       (yes)
    E121-16  Support the optional FROM clause in <fetch statement>.          (yes)
    E122     Scrollable cursors.                                             No
    E122-1   Read-only scrollable cursor support.                            No
    E122-2   Read-write scrollable cursor support.                           No
    E122-3   FETCH with explicit NEXT.                                       No
    E122-4   FETCH FIRST.                                                    No
    E122-5   FETCH LAST.                                                     No
    E122-6   FETCH PRIOR.                                                    No
    E122-7   FETCH ABSOLUTE.                                                 No
    E122-8   FETCH RELATIVE.                                                 No
    E123     <table reference> in <delete statement: positioned>, <delete    No
             statement: searched>, <insert statement>, <update statement:
             positioned> and <update statement: searched>.
    E131     Null value support (nulls in lieu of values).                   YES
    E141     Basic integrity constraints.                                    YES
    E141-1   NOT NULL constraints.                                           (yes)
    E141-2   UNIQUE constraints of NOT NULL columns.                         (yes)
    E141-3   PRIMARY KEY constraints.                                        (yes)
    E141-4   Basic FOREIGN KEY constraint with the NO ACTION default for     (yes)
             both referential delete action and referential update action.
    E141-6   CHECK constraints.                                              (yes)
    E141-7   Column defaults.                                                (yes)
    E141-8   NOT NULL inferred on UNIQUE and PRIMARY KEY.                    (yes)
    E141-9   Named constraints.                                              (yes)
    E141-10  Referential name order (names in a foreign key can be specified (yes)
             in any order).
    E142     Referential delete actions.                                     No
    E143     UNIQUE constraints of possibly null columns.                    No
    E151     Transaction support.                                            YES
    E151-1   <commit statement>.                                             (yes)
    E151-2   <rollback statement>.                                           (yes)
    E151-4   Support for the READ ONLY and READ WRITE clauses on the SET     (yes)
             TRANSACTION statement.
    E151-5   Support for the READ ONLY and UPDATE clauses on the DECLARE     (yes)
             CURSOR statement.
    E151-6   A <query expression> is updatable even though its <where        (yes)
             clause> contains a <subquery>.
    E151-7   Allow the word WORK not to be specified.                        (yes)
    E152     Basic SET TRANSACTION statement.                                YES
    E152-1   SET TRANSACTION ISOLATION LEVEL SERIALIZABLE.                   (yes)
    E152-2   SET TRANSACTION statement, <transaction access mode> clause.    (yes)
    E152-3   SET TRANSACTION statement, <diagnostics size> clause.           (yes)
    E153     Transaction isolation levels other than SERIALIZABLE.           No
    E161     SQL comments using double <minus sign>.                         YES
    E162     Bracketed SQL comments (/*...*/ comments).                      No
    E171     SQLSTATE support.                                               YES
    E182     Module language.                                                YES
    E191     Basic flagging.                                                 YES
    F021     Basic information schema (Support of the COLUMNS, TABLES and    YES
             VIEWS views in the INFORMATION_SCHEMA).
    F031     Basic schema manipulation with RESTRICT option.                 YES
    F031-1   CREATE TABLE statement to create persistent base tables.        (yes)
    F031-2   CREATE VIEW statement.                                          (yes)
    F031-3   GRANT statement.                                                (yes)
    F031-4   ALTER TABLE statement, ADD COLUMN clause.                       (yes)
    F031-8   ALTER TABLE statement, ALTER COLUMN clause.                     (yes)
    F031-9   ALTER TABLE statement, ADD CONSTRAINT clause.                   (yes)
    F031-10  ALTER TABLE statement, DROP CONSTRAINT clause.                  (yes)
    F031-13  DROP TABLE statement, RESTRICT clause.                          (yes)
    F031-16  DROP VIEW statement, RESTRICT clause.                           (yes)
    F031-19  REVOKE statement, RESTRICT clause.                              (yes)
    F031-20  DROP TYPE statement, RESTRICT clause.                           (yes)
    F031-21  DROP ROUTINE statement, RESTRICT clause.                        (yes)
    F032     Basic schema manipulation with CASCADE option.                  No
    F032-1   DROP TABLE statement, CASCADE clause.                           No
    F032-2   DROP VIEW statement, CASCADE clause.                            No
    F032-3   DROP TYPE statement, CASCADE clause.                            (yes)
    F032-4   DROP ROUTINE statement, CASCADE clause.                         (yes)
    F032-5   REVOKE statement, CASCADE clause.                               No
    F033     ALTER TABLE statement, DROP COLUMN.                             No
    F033-1   ALTER TABLE statement, DROP COLUMN CASCADE clause.              No
    F033-2   ALTER TABLE statement, DROP COLUMN RESTRICT clause.             (yes)
    F034     Full REVOKE statement.                                          No
    F034-1   REVOKE statement performed by an <authorization identifier>     No
             other than the owner of a schema object.
    F034-2   REVOKE statement, GRANT OPTION FOR clause.                      No
    F034-3   REVOKE statement to revoke a privilege that the grantee has     No
             WITH GRANT OPTION.
    F041     Basic joined table.                                             YES
    F041-1   Inner join (but not necessarily the INNER keyword).             (yes)
    F041-2   INNER keyword.                                                  (yes)
    F041-3   Left Outer Join.                                                (yes)
    F041-4   Right Outer Join.                                               (yes)
    F041-5   Outer joins can be nested.                                      (yes)
    F041-6   Column names in ON clause can be in different order than those  (yes)
             in the OUTER JOIN clause.
    F041-7   The inner table in a left or right outer join can also be used  (yes)
             in an inner join.
    F041-8   All comparison operators are supported (rather than just =).    (yes)
    F051     Basic date & time.                                              YES
    F051-1   DATE data type (including support of DATE literal).             (yes)
    F051-2   TIME data type (including support of TIME literal) with         (yes)
             fractional seconds precision of at least 0.
    F051-3   TIMESTAMP data type (including support of TIMESTAMP literal)    (yes)
             with fractional seconds precision of at least 0 and 6.
    F051-4   Comparison predicate on like date & time data types.            (yes)
    F051-5   Explicit CAST between datetime types and CHARACTER & CHARACTER  (yes)
             VARYING.
    F051-6   CURRENT_DATE.                                                   (yes)
    F051-7   CURRENT_TIME.                                                   (yes)
    F051-8   CURRENT_TIMESTAMP.                                              (yes)
    F052     Interval data type.                                             No
    F081     UNION in views.                                                 YES
    F121     Get diagnostics.                                                No
    F131     Grouped operations.                                             YES
    F131-1   Even though a table in the FROM clause is a grouped view, the   (yes)
             query can contain a WHERE, GROUP BY or HAVING.
    F131-2   Even though a table in the FROM clause is a grouped view,       (yes)
             multiple tables can be specified in the query.
    F131-3   Even though a table in the FROM clause is a grouped view, the   (yes)
             select list can contain a <set function>.
    F131-4   A subquery within a comparison predicate cannot contain a GROUP (yes)
             BY clause or a HAVING clause and can identify a grouped view.
    F131-5   The table in the FROM clause of a single row SELECT statement   (yes)
             can be a grouped view. Also a single row SELECT statement may
             specify a GROUP BY clause or HAVING clause.
    F171     Multiple schemas per user.                                      YES
    F181     Multiple module support (the ability to associate multiple host YES
             compilation units with a single SQL-session at one time).
    F201     CAST functions (excluding support for casting the INTERVAL data YES
             type).
    F221     Explicit defaults.                                              YES
    F222     DEFAULT VALUES support in an <insert statement>.                No
    F231     Privilege Tables.                                               No
    F231-1   TABLE_PRIVILEGES view.                                          No
    F231-2   COLUMN_PRIVILEGES view.                                         No
    F231-3   USAGE_PRIVILEGES view.                                          No
    F251     Domain support.                                                 No
    F261     CASE expression.                                                YES
    F261-1   <simple case>.                                                  (yes)
    F261-2   <searched case>.                                                (yes)
    F261-3   NULLIF.                                                         (yes)
    F261-4   COALESCE.                                                       (yes)
    F271     Compound character literals.                                    No
    F281     LIKE enhancements.                                              No
    F291     UNIQUE predicate.                                               No
    F301     <corresponding specification> in <query expression>s.           No
    F302     INTERSECT DISTINCT table operator.                              No
    F303     INTERSECT ALL table operator.                                   No
    F311     Schema definition statement.                                    YES
    F321     User authorization.                                             No
    F331     Constraint tables.                                              YES
    F331-1   TABLE_CONSTRAINTS view.                                         (yes)
    F331-2   REFERENTIAL_CONSTRAINTS view.                                   (yes)
    F331-3   CHECK_CONSTRAINTS view.                                         (yes)
    F341     Usage tables.                                                   No
    F361     User authorization.                                             No
    F381     Extended schema manipulation.                                   No
    F391     Long identifiers.                                               No
    F401     Full outer join.                                                No
    F401-1   Natural Join.                                                   No
    F411     Time zone specification.                                        No
    F421     National character.                                             No
    F441     Extended set function support.                                  No
    F451     Character set definition.                                       No
    F461     Named character sets.                                           No
    F471     Scalar subquery values.                                         YES
    F481     Expanded NULL predicate.                                        YES
    F491     Constraint management.                                          No
    F501     Features and conformance tables.                                YES
    F501-1   SQL_FEATURES.                                                   (yes)
    F501-2   SQL_SIZING.                                                     (yes)
    F511     BIT data type.                                                  No
    F521     Assertions.                                                     No
    F531     Temporary tables.                                               No
    F551     Full datetime.                                                  No
    F561     Full value expressions.                                         No
    F571     Truth value tests.                                              No
    F581     The POSITION function for use with CHARACTER, CHARACTER VARYING No
             and LOB data types.
    F611     Indicator data types.                                           No
    F641     Row and table constructors.                                     No
    F651     Catalog name qualifiers.                                        No
    F661     Simple tables.                                                  No
    F671     Subqueries in CHECK.                                            No
    F681     Union and cross join.                                           No
    F691     Collation and translation.                                      No
    F701     Referential update actions.                                     No
    F721     Deferrable constraints.                                         No
    F731     INSERT column privileges.                                       No
    F741     Referential MATCH types.                                        No
    F751     View CHECK enhancements.                                        No
    F761     Session management.                                             No
    F771     Connection management.                                          No
    F781     Self-referencing operations.                                    No
    F791     Insensitive cursors.                                            No
    F811     Extended flagging.                                              No
    F821     Local table references.                                         No
    F831     Full cursor update.                                             No
    T011     Timestamp in information schema for configuration management.   No
    T031     BOOLEAN data type.                                              No
    T041     Basic LOB data type support.                                    YES
    T041-1   BLOB data type.                                                 (yes)
    T041-2   CLOB data type.                                                 (yes)
    T041-3   LENGTH and SUBSTRING function support for LOB data types.       (yes)
    T041-4   concatenation of LOB data types.                                (yes)
    T041-5   non-holdable locator for LOB data types.                        (yes)
    T042     Extended LOB data type support.                                 No
    T042-1   OVERLAY function.                                               No
    T071     CASCADE option for DROP COLLATION.                              No
    T121     WITH (excluding RECURSIVE) in <query expression>.               YES
    T122     WITH RECURSIVE in <query expression>.                           No
    T131     Recursive query.                                                No
    T141     SIMILAR predicate.                                              No
    T151     DISTINCT predicate.                                             No
    T161     Optional interval qualifier.                                    No
    T171     LIKE clause in table definition.                                No
    T191     Referential action RESTRICT.                                    No
    T201     Comparable data types for referential constraints.              YES
    T211     Triggers.                                                       No
    T211-1   Support for triggers activated on UPDATE, INSERT, DELETE of     No
             one base table.
    T211-2   Support for BEFORE triggers that are applied before any         No
             modifications are made to the database. These triggers have
             access to old (delete, update) and new (insert, update) rows.
    T211-3   Support for AFTER triggers that are applied before any          No
             modifications are made to the database. These triggers have
             access to both old (delete, update) and new (insert, update)
             rows and transition tables.
    T211-4   Support for triggers that are to be applied once for each row   No
             of the subject table that is affected by the triggering SQL
             operation.
    T211-5   Ability to specify a search condition that must be true before  No
             the trigger is invoked.
    T211-6   Support for run-time rules for the interaction of triggers and  No
             constraints.
    T211-7   TRIGGER privilege.                                              No
    T211-8   Multiple triggers for the same the event are executed in the    No
             order in which they were created in the catalog.
    T212     Triggers applied once for the triggering statement.             No
    T221     WITH HOLD cursors.                                              YES
    T231     SENSITIVE cursors.                                              No
    T241     START TRANSACTION statement.                                    No
    T251     LOCAL option for SET TRANSACTION statement.                     No
    T261     Chained transactions.                                           No
    T271     Savepoints.                                                     No
    T281     SELECT privilege with column granularity.                       No
    T291     Static and Dynamic execution rights.                            No
    T301     Functional Dependencies.                                        No
    T321     Basic SQL-invoked routines.                                     YES
    T321-1   User-defined functions with no overloading.                     (yes)
    T321-2   User-defined stored procedures with no overloading.             (yes)
    T321-3   <routine invocation>.                                           (yes)
    T321-4   <call statement>.                                               (yes)
    T321-5   <return statement>.                                             (yes)
    T322     Overloading of SQL-invoked functions and SQL-invoked            No
             procedures.
    T331     Roles.                                                          No
    T361     User-defined aggregate operators.                               No
    T371     Quantified predicate extensions.                                No
    T391     Table name not required in <delete statement: positioned> or    No
             <update statement: positioned>.
    T401     INSERT into a cursor.                                           No
    T411     ROW may be specified in an UPDATE statement.                    No
    T421     Character Sets.                                                 No
    T431     CUBE and ROLLUP operations.                                     No
    T441     ABS and MOD functions.                                          No
    T461     Symmetric <between predicate>.                                  No
    T471     Result sets return value.                                       No
    O011     Minimum user-defined data type support (distinct types).        YES
    O021     Basic user-defined data types (Support for structured types     No
             (ADTs and named row types) with the exception of those features
             listed under Enhanced ADTs).
    O022     Enhanced user-defined data types.                               No
    O022-1   Constructor option.                                             No
    O022-2   Attribute default.                                              No
    O022-3   Multiple inheritance.                                           No
    O022-4   Public, private, protected specification on attributes.         No
    O022-5   Ordering clause in type definition.                             No
    O041     Reference types.                                                No
    O051     Create table of type.                                           No
    O061     ALTER TABLE <add named row type>.                               No
    O071     SQL paths in function and type name resolution.                 No
    O081     Subtables.                                                      No
    O091     Basic array support.                                            No
    O091-1   Arrays of built-in data types.                                  No
    O091-2   Arrays of distinct types.                                       No
    O092     Arrays of UDTs.                                                 No
    O094     Arrays of reference types.                                      No
    O111     ONLY in query expressions (to restrict subtable search).        No
    O121     Dereference operation (path expressions).                       No
    O131     Reference operation.                                            No
    O141     Attribute & field reference.                                    No
    O141-1   Observer reference.                                             No
    O141-2   Field reference.                                                No
    O151     Type predicate.                                                 No
    O161     <subtype treatment>.                                            No
    O171     Array expressions.                                              No
    O191     Basic SQL routines on user-defined types (with dynamic          No
             dispatch).
    O192     Basic SQL routines on user-defined types.                       No
    O192-1   Type preserving functions.                                      No
    O192-2   Generalized expressions.                                        No
    O201     SQL routines on arrays.                                         No
    O201-1   Array parameters.                                               No
    O201-2   Array as result type of functions.                              No
    O211     User-defined cast functions.                                    No
    O231     ADT locators.                                                   No
    O232     Array locators.                                                 No


Table Tax_2: SQL/CLI Feature Taxonomy
.....................................

::

    FEATURE  FEATURE                                                         CORE
    ID       DESCRIPTION                                                     SQL?
    C01      SQL/CLI.                                                        No

Table Tax_3: SQL/PSM Feature Taxonomy
.....................................

::

    FEATURE  FEATURE                                                         CORE
    ID       DESCRIPTION                                                     SQL?
    P01      Stored modules                                                  No
    P01-1    <SQL-server module definition>                                  No
    P01-2    <drop module statement>                                         No
    P02      Computational completeness                                      No
    P02-1    <compound statement>                                            No
    P02-2    <handler declaration>                                           No
    P02-3    <condition declaration>                                         No
    P02-4    <SQL variable declaration>                                      No
    P02-5    <assignment statement>                                          No
    P02-6    <case statement>                                                No
    P02-7    <if statement>                                                  No
    P02-8    <iterate statement>                                             No
    P02-9    <leave statement>                                               No
    P02-10   <loop statement>                                                No
    P02-11   <repeat statement>                                              No
    P02-12   <while statement>                                               No
    P02-13   <for statement>                                                 No
    P02-14   <signal statement>                                              No
    P02-15   <resignal statement>                                            No
    P02-16   <control statement>s as the SQL-statement of                    No
    P03      Information Schema views                                        No
    P03-1    MODULES view                                                    No
    P03-2    MODULE_TABLE_USAGE view                                         No
    P03-3    MODULE_COLUMN_USAGE view                                        No
    P03-4    MODULE_PRIVILEGES view                                          No

Table Tax_4: SQL/Bindings Feature Taxonomy
..........................................

::

    FEATURE  FEATURE                                                    CORE
    ID       DESCRIPTION                                                SQL?
    B011     Embedded Ada                                               (maybe)[1]
    B012     Embedded C                                                 (maybe)[1]
    B013     Embedded COBOL                                             (maybe)[1]
    B014     Embedded Fortran                                           (maybe)[1]
    B015     Embedded MUMPS                                             (maybe)[1]
    B016     Embedded Pascal                                            (maybe)[1]
    B017     Embedded PL/I                                              (maybe)[1]
    B021     Direct SQL                                                 No
    B031     Basic dynamic SQL                                          No
    B032     Extended dynamic SQL                                       No
    B032-1   <describe input> statement                                 No
    B041     Extensions to embedded SQL exception                       No
    B051     Enhanced execution rights                                  No

[Note 1] A conforming DBMS must support at least one embedded language if
embedded SQL is the binding style.
