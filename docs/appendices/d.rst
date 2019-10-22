.. highlight:: text

===========================================
Appendix D -- Incompatibilities with SQL-92
===========================================

SQL3 is compatible with the former version of the Standard (SQL-92) except in
the following cases.

* In SQL-92, a <parameter declaration list> had a deprecated alternative
  ``<parameter declaration>...`` (i.e.: a parameter list not surrounded by
  parentheses and with the component parameter declarations not separated by
  commas). SQL3 does not contain this option.

* In SQL-92, if one or more rows deleted or updated through some Cursor are
  later updated or deleted through some other Cursor by a <delete statement:
  searched>, by an <update statement: searched> or by some <update rule> or
  <delete rule> of some <referential constraint definition>, no exception
  condition is raised and no completion condition (other than successful
  completion) is raised. In SQL3, a completion condition is raised:
  warning-cursor operation conflict.

* In SQL-92, there were two <status parameter>s provided: the deprecated
  ``SQLCODE`` and ``SQLSTATE``. SQL3 does not support the ``SQLCODE`` <status 
  parameter> and ``SQLCODE`` is no longer a reserved <keyword>.

* SQL-92 allowed you to omit the semicolon at the end of <module contents>;
  listing this as a deprecated feature. In SQL3, the semicolon at the end of
  <module contents> is mandatory.

* In SQL-92, it was possible for applications to define new Character sets,
  Collations and Translations. In SQL3, those capabilities are limited to
  defining new Character sets, Collations and Translations that are identical to
  existing Character sets, Collations and Translations, respectively, except for
  their names and other minor details.

* In SQL-92, it was possible for applications to specify the Character set
  associated with an <identifier> using: ``_<Character set specification>``. 
  SQL3 no longer supports that capability.

* In SQL-92, it was possible to sort a Cursor by a Column's ordinal position
  in the Cursor. SQL3 no longer supports that capability.

* SQL3 contains more reserved <keyword>s than SQL-92. The new reserved
  <keyword>s are:

::

    ABS
    ACTION
    AFTER
    AGGREGATE
    ALIAS
    ARRAY
    BEFORE
    BINARY
    BLOB
    BOOLEAN
    BREADTH
    CALL
    CARDINALITY
    CLOB
    COMPLETION
    CONCATENATE
    CUBE
    CURRENT_PATH
    CYCLE
    DATA
    DEPTH
    DEREF
    DESTROY
    DICTIONARY
    EACH
    EQUALS
    EVERY
    FACTOR
    FREE
    GENERAL
    GROUPING
    HOLD
    HOST
    IGNORE
    INITIALIZE
    ITERATE
    LESS
    LARGE
    LIMIT
    LOCATOR
    MOD
    MODIFIES
    MODIFY
    NCLOB
    NEW
    NO
    NONE
    OBJECT
    OFF
    OLD
    OPERATION
    OPERATOR
    ORDINALITY
    OVERLAY
    PARAMETER
    PARAMETERS
    PATH
    PREORDER
    READS
    RECURSIVE
    REF
    REFERENCING
    REPLACE
    RESULT
    RETURN
    RETURNS
    ROLLUP
    ROLE
    ROUTINE
    ROW
    SAVEPOINT
    SEARCH
    SENSITIVE
    SEQUENCE
    SESSION
    SETS
    SIMILAR
    SPACE
    SPECIFIC
    SPECIFICTYPE
    SQLEXCEPTION
    SQLWARNING
    START
    STATE
    STRUCTURE
    SUBLIST
    SYMBOL
    TERM
    TERMINATE
    THE
    TREAT
    TRIGGER
    TYPE
    UNDER
    VARIABLE
    WITHOUT
