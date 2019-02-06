.. highlight:: text

====================
Appendix G -- Errata
====================

This concise errata list concerns apparent errors in some of our source 
literature, such as the SQL standard documents or the ODBC manual. We do not 
intend this as a comment. Like any errata list, its sole use is to help you 
avoid confusion if you happen to read one of those texts. And, like any errata 
list, it's ephemeral. At some time, the original documents will cease to 
contain these errors. 

.. rubric:: Table of Contents

.. contents::
    :local:

SQL Foundation
==============

* The data type and size of ``CURRENT_ROLE`` is not defined, but we have 
  assumed that it's supposed to match the data type and size defined for 
  ``CURRENT_USER``. 

* The Standard declares that precision is the number of "significant digits". 
  We have to assume they don't use the usual definition of significant. 

* The Standard speaks of valid datetime or interval results "according to the 
  Gregorian calendar". But the Gregorian calendar only validates dates. We 
  assume they mean "based on a 24 hour clock" for times, with adjustments 
  according to the Gregorian calendar in the case of timestamps and (where 
  applicable) intervals. 

* The word "satisfies" means "is ``TRUE``" when the context is the ``HAVING`` 
  clause, or "is not ``FALSE``" when the context is a constraint. But it is not 
  clear what "satisfies" means when the context is a ``WHEN`` clause or a 
  view's ``WITH CHECK OPTION`` clause. Therefore it is not possible to be sure 
  whether these clauses are "satisfied" if the search conditions that they 
  refer to are ``UNKNOWN``. 

* SQL3's ``BOOLEAN`` data type should have four values: ``TRUE``, ``FALSE``, 
  ``UNKNOWN`` and ``NULL``. 

* For "effect of replacing rows in base tables", the trigger event is defined 
  as ``DELETE``. We assume that ``UPDATE`` is meant. 

* The ``DROP TABLE ... CASCADE`` definition fails to specify that all dependent 
  triggers will also be dropped. The ``DROP TABLE ... RESTRICT`` definition 
  fails to specify that, if there are dependent triggers, the drop will fail. 
  Since analogous statements are true for ``DROP VIEW``, we assume that they 
  should also be true for ``DROP TABLE``. 

* The Standard states six times that the following statement, or a slight 
  variation thereof, is "implicit" (in column definitions etc.):
  
  ::
  
      "CREATE TRIGGER BTN BEFORE DELETE ON TND
        FOR EACH STATEMENT
        SET CONSTRAINT CCN DEFERRED"
  
  But ``SET CONSTRAINT`` statements are illegal within triggers.

* According to the Standard, ``DROP TRIGGER`` is legal in Core SQL; but 
  ``CREATE TRIGGER`` is illegal. We assume that the intent is not to include 
  ``DROP TRIGGER`` in Core SQL either. 

* In the description of <cast specification> there is a reference to an 
  ``SQLSTATE error 'Data exception - invalid interval format'``; this error 
  does not appear in the list of ``SQLSTATE`` exception conditions so we 
  haven't been able to provide an ``SQLSTATE`` code for it. 

* The ``ASCII_FULL`` character set does not include the ``\0`` character. This 
  contradicts FIPS, and makes casts from bit strings difficult. 

* The Standard's Section 9.7 <type name determination> has no mention of 
  ``BOOLEAN``. Neither does Section 10.14. ``BOOLEAN`` appears to have been 
  forgotten in many places. 

* There is an initial definition of "subtype". The Standard's description of 
  UDTs is comprehensible only if this definition is ignored. 

* The Standard's definition of "direct subtype" is confusing: 
  
  "A type ``T(a)`` 
  is a direct subtype of a type ``T(b)`` if ``T(a)`` is a proper subtype of 
  ``T(b)`` and there does not exist a type ``T(c)`` such that ``T(c)`` is a 
  proper subtype of ``T(b)`` and a proper subtype of ``T(a)``." 
  
  Perhaps it should read: 
  
  "A type ``T(a)`` is a direct subtype of a type ``T(b)`` if ``T(a)`` is a 
  proper subtype of ``T(b)`` and there does not exist a type ``T(c)`` such that 
  ``T(c)`` is a proper subtype of ``T(b)`` and a proper supertype of ``T(a)``." 
  
  If this emendation is correct, then the terms "every direct supertype" and 
  "every direct supertable" are misleading; more English are the terms "the 
  direct supertype" and "the direct supertable", passim. 

* The ``CREATE TYPE`` definition contains a contradiction:
  
  ::
  
    "4) If <subtype clause> is not specified, then <representation> shall be specified.
     5) If <subtype clause> is not specified, then NOT FINAL shall be specified.
     6) If <representation> specifies <predefined type>, then:
         a) ...
         b) FINAL shall be specified.
         c) <subtype clause> shall not be specified."
  
  We have made no assumption as to the Standard's intent here.

* The ``BNF`` nonterminal <method specification> is defined differently in two 
  separate sections. We have made no assumption as to which definition is the 
  correct one.

* For the ``NEW`` statement, the Standard contains this suspicious looking 
  grammer:
  
  ::
  
    "<new specification> ::= NEW <routine invocation>
    
       <new invocation> ::= <method invocation>"
  
  <new invocation> is not used elsewhere. We assume that the definition is 
  actually "``NEW`` <method invocation>".
  
  If this assumption is incorrect, the first syntax rule for the ``NEW`` 
  statement seems like it would work only for the main option:
  
  "1) Let ``RN`` be the <routine name> immediately contained in the <routine 
  invocation>. Let ``MN`` be the <qualified identifier> immediately contained in 
  ``RN``."
  
  Possibly what is meant is:
  
  "1) Let ``RN`` be the <routine name> immediately contained in the <routine 
  invocation> or <method invocation>. Let ``MN`` be the <qualified identifier> 
  immediately contained in ``RN``."

* This note looks out of place, and in any case is superseded by Note 243:

  "NOTE 242 - The comparison categories of two user-defined types in the same 
  type family must be the same."
  
  Possibly what is meant is:
  
  "NOTE 242 - The comparison forms of two user-defined types in the same 
  type family must be the same."

* The ``INFORMATION_SCHEMA.ATTRIBUTES`` view definition contains references to 
  ``TABLE_CATALOG`` and ``COLUMN_DEFAULT`` columns -- neither of which are 
  applicable here. We assume they should be ``UDT_CATALOG`` and 
  ``ATTRIBUTE_DEFAULT``. 

* The ``DEFINITION_SCHEMA.ATTRIBUTES`` base table is also defined as having two 
  columns -- ``TABLE_CATALOG`` and ``TABLE_SCHEMA`` -- which are not applicable 
  here. We assume they should be ``UDT_CATALOG`` and ``UDT_SCHEMA``. 
  
  Also, this table's columns ``USER_DEFINED_TYPE_CATALOG``, 
  ``USER_DEFINED_TYPE_SCHEMA`` and ``USER_DEFINED_TYPE_NAME`` are defined on 
  domain ``INFORMATION_SCHEMA.CHARACTER_DATA``. 
  
  But everywhere else, such columns are defined on domain 
  ``INFORMATION_SCHEMA.SQL_IDENTIFIER``. We assume the intent is to be 
  consistent here as well. 

* The ``NUMERIC_PRECISION_RADIX`` value for datetime / interval data types is 
  unclear. The ``GetTypeInfo`` description of the ODBC 3.0 manual says: "If the 
  data type is an approximate numeric type, this column contains the value 
  ``2`` to indicate that ``COLUMN_SIZE`` specifies a number of bits. For exact 
  numeric types, this column contains the value ``10`` to indicate that 
  ``COLUMN_SIZE`` specifies a number of decimal digits. Otherwise, this column 
  is ``NULL``." 
  
  The same section in the SQL/CLI document says:
  
  ::
  
    "r) The value of NUM_PREC_RADIX is
         Case:
         i) If the value of PRECISION is the value of a precision, then the radix of that precision.
         ii) Otherwise, the null value."
  
  While the definition of the ``DEFINITION_SCHEMA.DATA_TYPE_DESCRIPTOR`` base 
  table, where this information is stored has this constraint:
  
  ::
  
    "    CHECK (
         ...
         DATA_TYPE IN ( 'DATE', 'TIME', 'TIMESTAMP',
                        'TIME WITH TIME ZONE', 'TIMESTAMP WITH TIME ZONE' )
         ...
         AND ( NUMERIC_PRECISION, NUMERIC_PRECISION_RADIX ) IS NOT NULL"
  
  From the above quotes, some disagreements are visible:
  
   (a) The writers of ODBC thought datetime/interval radices are nullable.
   
   (b) The SQL/CLI writers had no idea ``PRECISION`` is a nonexistent column 
       but agree that radices can be nullable if a data type has no precision.
   
   (c) The foundation writers thought datetime/interval radices couldn't be ``NULL``.
  
  For ``GET_TYPE_INFO``, we assume the first two quotes reflect the true 
  intent: that ``NUMERIC_PRECISION_RADIX`` value for datetimes and intervals is 
  ``NULL``.

* The definition of the ``INFORMATION_SCHEMA.ROLE_ROUTINE_GRANTS`` view 
  contains:
  
  ::
  
       "SELECT
       ...
       ROUTINE_CATALOG, ROUTINE_SCHEMA, ROUTINE_NAME
       ...
       FROM ROUTINE_PRIVILEGES"
  
  But these three columns do not exist in the ``ROUTINE_PRIVILEGES`` table. We 
  assume these columns should be omitted from the view.

* The definition of the ``INFORMATION_SCHEMA.ROLE_USER_DEFINED_TYPE_GRANTS`` 
  view contains:
  
  ::
  
       "SELECT
       ...
       OBJECT_TYPE
       ...
       FROM DEFINITION_SCHEMA.USER_DEFINED_TYPE_PRIVILEGES"
  
  But this column does not exist the in ``USER_DEFINED_TYPE_PRIVILEGES`` table. 
  We assume this column should be omitted from the view.

SQL/CLI
=======

* The "Description of CLI item descriptors" says that ``DEFERRED`` is true if 
  the octet length pointer points to ``SQL NULL DATA``.

* For ``SQLGetTypeInfo``, ``NULL`` values are returned for ``sql_prefix`` and 
  ``sql_suffix`` -- i.e.: ``NULL`` is used to mean "blank string". In other 
  fields it means N/A.

* For ``SQLExecute`` and ``SQLExecute``, the general rules are ordered in such 
  a way that input parameters will be checked for consistency ``AFTER`` 
  execution. We assume that checking should take place before execution. The 
  embedded SQL document has parameter-checking in the logical place. 

* The ``SQLDisconnect`` function description contains a reference to an 
  exception "active SQL-statement"; we assume this should read "active 
  SQL-transaction". 

* The ``SQLGetData`` function description contains a reference to ``IP`` and 
  ``DP``, which do not exist. 

* The ``SQLSetDescField`` function description suggests that it is illegal to 
  set the ``SQL_DESC_TYPE`` field to ``SQL_SMALLINT``, ``SQL_INTEGER``, 
  ``SQL_REAL`` or ``SQL_DOUBLE_PRECISION`` (or several other legal data types). 
  This is clearly an oversight. 

* The ``SQLSetDescField`` function description fails to state that the 
  ``RecordNumber`` parameter should be ignored if ``FieldIdentifier`` is 
  ``SQL_DESC_COUNT``. We assume this is the case. 

* The ``SQLGetDescRec`` function description is ambiguous about the field to be 
  used as the source for Length. 

* For ``SQLGetDiagField``, the Standard says ``SQL_DIAG_MORE`` is associated 
  with a return of ``'Y'`` or ``'N'``. But ``SQL_DIAG_MORE`` is not defined as 
  a string. 

* For ``SQLGetLength``: exception "Invalid argument value" is undefined. 

* For ``SQLColumns``: for a <fractional seconds precision>, the value is taken 
  from ``INFORMATION_SCHEMA.COLUMNS.NUMERIC_PRECISION``. The value is actually 
  in ``INFORMATION_SCHEMA.COLUMNS.DATETIME_PRECISION`` and we assume this is 
  the intent. Also: the ``SQL_DATA_TYPE`` column has been forgotten; we assume 
  it is included. Also: for calculating ``SQL_DATETIME_SUB``, the Standard says 
  one is supposed to use ``INFORMATION_SCHEMA.COLUMNS.DATA_TYPE`` to look up a 
  ``'Code'`` -- however, the information is actually in found in 
  ``INFORMATION_SCHEMA.COLUMNS.INTERVAL_TYPE``; we assume this is the intent. 

* There is an implicit assumption that ``CAST`` is possible between two 
  character sets (otherwise, why bother having character set in the 
  descriptor IDA?). But ``CAST`` is illegal if repertoires differ.
