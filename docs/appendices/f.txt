.. highlight:: text

======================
Appendix F -- Glossary
======================

The entries in this glossary include the computer-related words, names,
acronyms, abbreviations, SQL keywords and official terms used in this book, as
well as those that are common in the SQL/database industry. Each entry is
sorted in ascending ASCII order and may contain one or all of the following:

## a "see" reference to a preferred term;

## a "see also" reference to related or near-synonymous terms;

## a context indicator, e.g.: "ODBC term"; important because different
vocabularies are used in different circles.

.. rubric:: Table of Contents

.. contents::
    :local:

Glossary Entries
================

`` ``
    SQL special character; used as a delimiter. Standard name: "space".

``!``
    Non-standard special character. Usual name: "exclamation mark".

``!=``
    Non-standard special character. This symbol means "not equal" in C and Oracle
    programs, but has no meaning in Standard SQL. See also: <>.

``#``
    Non-standard special character. Usual name: "number sign". Also called:
    octothorpe, hash sign.

``$``
    Non-standard special character. Usual name: "dollar sign".

``@``
    Non-standard special character. Usual name: "commercial at sign".

``"``
    SQL special character; used to surround a delimited identifier. Standard name:
    "double quote mark". Also called (in Unicode): quotation mark.

``%``
    SQL special character; used to specify a LIKE pattern. Standard name: "percent
    sign".

``&``
    SQL special character; used only in MUMPS programs. Standard name:
    "ampersand".

``'``
    SQL special character; used to surround a character string literal. Standard
    name: "quote mark". Also called (in Unicode): apostrophe, single quote.

``(``
    SQL special character; used to mark the start of a list. Standard name: "left
    parenthesis".

``)``
    SQL special character; used to mark the end of a list. Standard name: "right
    parenthesis".

``*``
    SQL special character. Standard name: "asterisk".

    [1] In arithmetic, the multiply operator.

    [2] After SELECT, a shorthand for: all columns.

``+``
    SQL special character; the arithmetic add operator or unary plus operator.
    Standard name: "plus sign".

``,``
    SQL special character; used to separate items in a list. Standard name:
    "comma".

``-``
    SQL special character; the arithmetic subtract operator or unary minus
    operator. Standard name: "minus sign". Also called (in Unicode): hyphen-minus.

``.``
    SQL special character; used to separate parts of a name. Standard name:
    "period". Also called (in Unicode): full stop.

``...``
    Non-standard special character. Usual name: "ellipsis".

    [1] This symbol is not used in Standard SQL, but in BNF descriptions, an
    ellipsis indicates a repeatable portion of syntax. See also: BNF.

    [2] In the text of this book, we frequently use an ellipsis to indicate that
    we have omitted some details in an example for the sake of brevity.

``/``
    SQL special character; the arithmetic divide operator. Standard name:
    "solidus". Also called: division sign, slash.

``/*``
    SQL token; indicates a comment. The use of ``/* comments */`` is new in SQL3. See
    also: BRACKETED COMMENTS.

``:``
    SQL special character; prefaces a host variable or parameter. Standard name:
    "colon".

``;``
    SQL special character; terminates an SQL statement. Standard name:
    "semicolon".

``<``
    SQL special character; the "less than" operator.

``<=``
    SQL "less than or equals" operator.

``<>``
    SQL "not equals" operator.

``=``
    SQL special character; the "equals" operator.

``>``
    SQL special character; the "greater than" operator.

``>=``
    SQL "greater than or equals" operator.

``?``
    SQL special character; the parameter marker. Standard name: "question mark".

A
-

ABANDONED
    An abandoned Privilege is derived from a Privilege that no longer exists. For
    example: Sam grants to Joe; Joe grants to Sally; Sam revokes from Joe; now
    Sally's Privilege is abandoned. For the same sort of reason (specifically loss
    of SELECT Privilege) there may also be "abandoned Views".

ABS
    An SQL3 keyword. The ABS function returns the absolute value of a number or an
    interval. Absolute values measure magnitude. Therefore they are always
    positive.

ABSOLUTE
    [1] An SQL Standard term. An absolute number is a base-1 number, so "FETCH ...
    ABSOLUTE 1" gets the first row in a result set. Compare: RELATIVE.

ABSTRACT
    Without reference to equivalents in the material world.

ABSTRACT DATA TYPE
    An Object/Relational term. Obsolete. Abbreviation: ADT. A type of UDT which is
    not instantiable.

ACCENTED LETTER
    An alphabetic character with a mark above it (acute or macron or breve or
    circumflex or grave or tilde or diaeresis) or below it (cedilla or ogonek) or
    through it (stroke). An accented letter is not a simple Latin letter.

ACCESS
    [1] Retrieval of a value from a field.

    [2] Opening a file.

    [3] Connecting.

    [4] Microsoft DBMS with some SQL-like features.

ACCESS ERROR
    Error ("exception condition") returned due to violation of an access rule,
    usually because appropriate Privileges are missing.

ACCESS MODE
    (Of a transaction) One of: READ-ONLY or READ-WRITE.

ACCESS PLAN
    [1] The sequence of steps that a DBMS optimizer chooses for a selection. For
    example: find rows of table#1 within index, then find rows of table#2 within
    index, then sort/merge the matchlists. Sometimes the access plan is shown by
    the non-standard EXPLAIN command. In usual practice, the access plan is not
    executable code. Also known as "access path".

    [2] An ODBC term. A plan for execution of any SQL statement, equivalent to a
    compiler's output. We deprecate meaning [2].

ACCESS PRIVILEGE
    See: PRIVILEGE.

ACCESS RULE
    An SQL Standard term. An access rule declares what conditions -- such as user
    Privileges -- must exist for execution to be legal. See also: GENERAL RULE,
    SYNTAX RULE.

ACCURATE
    (Of a value) Closely reflecting the actual value in the real world. See also:
    PRECISE.

ACID
    Abbreviation for the features of an ideal transaction: Atomic, Consistent,
    Isolated, Durable.

ACMO
    Abbreviation for Accredited Standards Making Organization.

ACTION
    [1] An SQL Standard term. The activity which you grant or revoke Privilege on,
    including one of these keywords: INSERT, UPDATE, DELETE, SELECT, REFERENCES,
    USAGE, UNDER, TRIGGER, EXECUTE.

    [2] See: REFERENTIAL ACTION.

    [3] See: TRIGGER.

ACTION QUERY
    An MS-Access term. See: DATA CHANGE STATEMENT.

ACTIVATED
    (Of a Trigger) Executable due to fulfillment of the conditions for database
    modification declared when the Trigger was defined.

ACTIVE
    [1] An SQL Standard term. A stmt is active if a Cursor is open, or if the stmt
    is associated with a deferred parameter number.

    [2] An ODBC term. A stmt is active if there are results pending from a query,
    or if UPDATE|INSERT|DELETE has happened, or if there is a wait for data due to
    a SQL_NEED_DATA parameter. Often it would be clearer to use the phrase
    "transaction in progress".

ACTIVE CONDITION
    A PSM term. The condition whose status code is returned in SQLSTATE. There may
    be several conditions in the diagnostics area, but only one is "active": the
    one with the highest priority.

ACTIVE RULE
    See: TRIGGER.

ADMIN
    An ADMIN OPTION is the equivalent, for a Role, of a GRANT OPTION.

ADT
    See: ABSTRACT DATA TYPE.

AFNOR
    Abbreviation for Association fran‡aise de normalisation.

AGENT
    Or SQL-agent. A job started by a user, which is bound to a client job, which
    calls a server. So essentially an agent is an instance of the user's
    application program. (In direct SQL the agent would be part of the
    implementation, though.)

AGGREGATE FUNCTION
    See: SET FUNCTION.

AGGREGATION
    Looking at a set of values which will be used in combination or
    interchangeably (due to a CASE expression, a set operator or an array
    concatenation). The rules of aggregation determine what the result data type
    is.

AGGREGATION RULE
    A rule affecting validity and implicit cast operations when multiple values
    are squeezed into the same Column, as for example in the result Table of a set
    operation.

AGREE
    An SQL Standard term, but unpopular. See the preferred term: DUPLICATE.

ALGORITHM
    The steps, rules or processes which define how inputs should be converted to
    outputs. Originally algorithms were for people (e.g. the long division
    algorithm), but the word is now almost exclusively applied to computer
    routines.

ALIAS
    [1] (Obsolete) temporary name in the FROM clause. See: CORRELATION NAME.

    [2] (referring to Triggers) an alternate name for an object whose "before" and
    "after" states are distinguishable due to Trigger operation.

ALL
    A modifier placed after a comparison operator and before a subquery,
    indicating that the comparison must be true "for all occurrences". Example: "a
    >= ALL (SELECT b FROM c)". The fancy name for ALL is: the universal
    quantifier. See also: ANY.

ALL PRIVILEGES
    SQL Standard term. The set of Privileges for which the grantor holds a grant
    option; thus, may not be the same as all possible or legal Privileges.

ALLOCATE
    Obtain system resources. In the CLI the main allocation function is
    SQLAllocHandle, which is used for new envs, dbcs, stmts and descs.

ALLOCATED SQL-CONNECTION
    See: dbc.

ALLOCATED SQL-ENVIRONMENT
    See: env.

ALLOCATED SQL statement
    See: stmt.

ALPHABET
    An ordered set of letters which may appear in a dictionary for a language. For
    example the current Latin alphabet is ABCDEFGHIJKLMNOPQRSTUVWXYZ. The
    characters - and . and _ are not alphabetic. The official definition of
    alphabetic is: whatever the ISO 10646 standard document says is alphabetic.

ALTER
    An SQL verb: to change a definition. SQL Objects that may be altered include:
    Tables, Domains.

ALTERNATE KEY
    A candidate key which is not a primary key.

AMERICAN NATIONAL STANDARDS INSTITUTE
    See: ANSI.

AMERICAN STANDARD CODE FOR INFORMATION INTERCHANGE
    See: ASCII.

ANNEX
    A part of the official SQL Standard which attempts to explain or inform,
    rather than legislate. For example: in the SQL-89 standard, everything about
    host-language embedding was put in Annexes.

ANSI
    American National Standards Institute. A quango umbrella. The NCITS (ANSI
    X3H2) committee, which works on SQL Standards, works for an organization named
    X3, which is overseen by ANSI. Their main documents are ANSI X3.135-1992 (the
    SQL-92 Standard), plus later additions and corrigenda. Web site: www.ansi.org.

ANY
    A modifier placed after a comparison operator and before a subquery,
    indicating that the comparison must be true "for any occurrences". Example: "a
    >= ANY (SELECT b FROM c)". The fancy name for ANY is: the existential
    quantifier. See also: ALL.

APD
    See: APPLICATION PARAMETER DESCRIPTOR.

API
    Windows term. Application Programming Interface. The definition of the public
    routines in a program library, including: names, parameter sizes, order in
    which parameters are passed, whether the stack should be restored on return
    and what the routine should return if it is a function call. ODBC is an
    example of an API for SQL. See also: CLI.

APPLICABLE PRIVILEGE
    For a user or Role: the set of all Privileges for which the user or Role is
    the grantee, or for which PUBLIC is the grantee. The word "applicable" is used
    here in the sense of "can be applied", not in the sense of "relevant".

APPLICATION
    [1] A host-language program which connects with SQL.

    [2] The software that a user sees. The application is what you write; the DBMS
    is what you interface the application with.

    [3] An SQL program written with the module language or the PSM (in this book
    we never use "application" in this sense). See also: AGENT.

APPLICATION DESC
    One of: APD or ARD.

APPLICATION PARAMETER DESCRIPTOR
    A CLI term. Often abbreviated APD. The APD is the description of a statement's
    parameters "as seen by the application". The APD is a desc, it is
    automatically allocated when you call SQLAllocHandle(SQL_HANDLE_STMT,...). It
    is one of four automatically-allocated descriptor areas. The others are: ARD,
    IRD, IPD.

APPLICATION ROW DESCRIPTOR
    A CLI term. Often abbreviated ARD. This is a structure containing:

    ::

        SQL_DESC_COUNT                maximum number of IDAs
        ...
          IDA OCCURS COUNT TIMES      "item descriptor area" multiple occurrence
            SQL_DESC_TYPE                 = data type
            SQL_DESC_OCTET_LENGTH         = number of bytes
            SQL_DESC_LENGTH               = number of characters or positions
            SQL_DESC_DATA_POINTER         = address of host variable
            SQL_DESC_OCTET_LENGTH_POINTER = address of size in octets
            ...

    The ARD is the description of the host program application buffers which are
    bound to result set's Columns; thus it's the row descriptor "as seen by the
    application". It is one of four automatically-allocated descriptor areas. The
    others are: APD, IRD, IPD.

APPROXIMATE NUMERIC
    One of the three numeric data types: REAL, FLOAT or DOUBLE PRECISION.
    Approximate numeric literals are represented in exponential notation, e.g.
    -1E-01. Conceivably internal storage is done according to IEEE floating-point
    regulations.

ARGUMENT
    A scalar expression which appears between the parentheses for a scalar
    function or a set function or a routine. The word "argument" properly refers
    to a specific value of a variable, for example if you use "function(x)" and x
    is 5, then x is the variable and 5 is the argument. See also: PARAMETER.

ARITHMETIC
    The study of numbers and the operations which apply to numbers. The main
    arithmetic operators are represented by the symbols + / * -.

ARRAY
    [1] A multiple-occurrence sequence of scalars, all of the same data type, is a
    one-dimensional array. An array of structures, with headings at the top, is a
    Table.

    [2] (SQL3) A data type constructed using the specification ARRAY. Arrays are
    an example (in fact the only current example) of a collection type.

ARD
    See: APPLICATION ROW DESCRIPTOR.

ASCENDING
    Going up. In an ascending sort sequence, the number 5 comes after 4 in the
    number sequence, and the letter 'K' comes after 'G' in the alphabet. Opposite
    is descending. Short form (used in SQL) is ASC.

ASCII
    American Standard Code for Information Interchange. A seven-bit standard
    encoding. ASCII values are equivalent to the first 128 values of the ISO
    8859-1 character set.

ASCII_FULL
    Also called: ISO8BIT. In SQL3 and the FIPS specification: a predefined
    character set containing the 256 graphic and non-graphic characters of the ISO
    8859-1 standard -- except \0.

ASCII_GRAPHIC
    Also called: GRAPHIC_IRV. In SQL3 and the FIPS specification: a predefined
    character set containing the 95 graphic characters of the ISO 646 standard
    (default values). ASCII_GRAPHIC is the same as SQL_CHARACTER with the addition
    of these characters: !#$@[\]^`{}~

ASENSITIVE CURSOR
    It is implementation-dependent whether changes to significant data are visible
    if a Cursor is asensitive. See also: SENSITIVE CURSOR, INSENSITIVE CURSOR.

ASSERTION
    [1] An expression definition which causes an assembler or compiler to generate
    an error if the result is not true.

    [2] An SQL Object containing a CHECK clause, which is defined with CREATE
    ASSERTION. Such Assertions are Constraints. The other kinds of Constraints are
    Table Constraints and Domain Constraints.

ASSIGN
    Copy a value from a source to a target, as in a COBOL "MOVE".

ASSIGNABLE
    Can be assigned, because data types have relevant characteristics in common.
    For example: a SMALLINT can be assigned to a DECIMAL (provided there is no
    overflow), and a CHAR can be assigned to a CHAR (assuming the same
    repertoires).

ASSIGNMENT STATEMENT
    A PSM term. See: SET STATEMENT.

ASSOCIATE
    Travel together with, have frequent dealings with, be part of the same
    structure, participate in the same process, link exclusively. The term appears
    frequently in the Standard but appears to have no technical meaning.

ASSOCIATIVE
    Unaffectable by order of execution, for example A+(B+C) yields the same result
    as (A+B)+C. See also: COMMUTATIVE.

ASYNCHRONOUS
    Can be executed when the DBMS feels like getting around to it. Asynchronous
    operations tend to be slow and non-critical.

ATOMIC SUBQUERY
    See: SCALAR SUBQUERY.

ATOMIC TRANSACTION
    A transaction which may perform operations on multiple rows or which may
    contain multiple updating statements, but which is not splittable. SQL
    transactions are all-or-nothing. Because they are not splittable, either all
    operations go through, or none do. Atomicity is one of the ACID transaction
    features.

ATOMIC VALUE
    A value whose degree and cardinality are both 1. A more common term is: scalar
    value.

ATTRIBUTE
    [1] A relational term. An attribute is a characteristic of an entity, for
    example a star's name and distance. This is a box into which we could put
    scalar values: for example 'Vega' and '7 light years' could constitute an
    occurrence of the attribute. See also: COLUMN, RELATION.

    [2] A CLI term. A setting for an env, dbc or stmt. Formerly called an
    "option".

    [3] [Obsolete] a Domain Constraint.

    [4] An SQL Standard term. A named component of an abstract data type
    descriptor. Attributes have data types, default values and nullability
    characteristics. Attribute values can only be accessed via observer functions
    and can only be changed via mutator functions, i.e.: they are encapsulated.

AUGMENTED
    (Of a method) Having a first parameter named SELF.

AUTHORIZATION
    See: PRIVILEGE DESCRIPTOR.

AUTHORIZATION_IDENTIFIER
    Also AUTHORIZATION ID or AUTHORIZATIONID. An identifier of a person or group
    who/which: (a) connected to a data source, and/or (b) owns one or more
    Schemas; and/or (c) has been granted Privileges. All Modules have an
    authorization_identifier. In SQL3, an authorization identifier is either a
    user identifier or a Role name.

AUTOMATIC COMMIT
    Also AUTO-COMMIT. A mode, the opposite of MANUAL COMMIT. In auto-commit mode,
    all UPDATE/DELETE/INSERT statements take effect immediately as if the
    statement was immediately followed by a COMMIT. However, Cursors are not
    closed. Auto-commit is the default in ODBC, but manual commit is the default
    in standard SQL. In some DBMSs auto-commit is effectively the default before
    and after all DDL statements (DDL statements are treated as transactions on
    their own).

AUTOMATIC DESC
    One of the four automatically-allocated descs associated with a stmt. As
    opposed to: USER DESC.

AVG
    An SQL set function, short for "average", which returns the arithmetic mean
    for a columnar expression.

B
-

BACKUP
    To make a copy of a Table's data or of an entire database, so that it can be
    recovered if accident occurs.

BACKUS-NAUR
    See: BNF.

BAG
    An object oriented term, used for OQL. See: MULTISET.

BASE
    (Of a number) See: RADIX.

BASE TABLE
    A Table which is not a View of another Table. In a straightforward system,
    there is some association of Base tables with files.

BASIC PREDICATE
    A predicate containing any comparison operator, or BETWEEN, or IN, or IS NULL
    or MATCH.

BASIC RESULT
    An SQL Standard term. See: RETURN CODE.

BATCH
    An ODBC term. You can pass several SQL statements in one string to an
    SQLExecDirect call. This is not standard behaviour and many DBMSs do not allow
    it.

BETWEEN
    An SQL relational operator or predicate. A is between B and C if A>=B and
    A<=C.

BINARY
    Based on 2 (compare: decimal which is based on 10, hexadecimal which is based
    on 16). The "binary relationship model" is a conceptual database design
    technique.

BINARY LARGE OBJECT
    The standard abbreviation is blob, but BLOB or BLOb are acceptable. Data type
    in SQL3, implemented by several vendors already, sometimes under different
    names. The vendor interpretations of the meaning of BLOBs differs. In some
    implementations a BLOB is not retrieved at the same time as the rest of the
    row; compare the dBASE "memo" type. The word LARGE only suggests typical use,
    in some DBMSs the maximum BLOB size is the same as the maximum CHAR or BIT
    size.

BINARY STRING
    A string which has an integral number of octets (this distinguishes BINARY
    from BIT strings), and which has no associated Character set (this
    distinguishes BINARY from CHAR strings). Since there is no Character set there
    is no Collation, therefore the only legal comparison operators are = and LIKE.
    All SQL binary strings are BLOBs.

BIND
    [1] To associate a host variable in a host-language application program with a
    parameter marker or select list Column in an SQL statement. With embedded SQL
    this may be part of the process of precompilation. With a CLI there will be
    descs involved.

    [2] To mix SQL statements with host language statements. This can be done in
    several ways. See: BINDING STYLE.

    [3] To associate an SQL statement's identifiers with the Objects of a Catalog
    definition, so that an access plan can be formed. Often the last step of
    precompilation. The SQLPrepare function binds a single SQL statement.

BINDING OFFSET
    An ODBC term. For those cases where a multiple-row fetch happens into an array
    buffer, the binding offset is the offset within the buffer where the data for
    the Column of row #n goes.

BINDING STYLE
    An SQL Standard term. The conventions used for interfacing an application with
    a DBMS. The primary alternatives are: Module, embedded (SQL/Bindings), direct,
    implementation-defined, call-level interface (CLI or SQL/CLI). The Persistent
    Stored Modules feature is not a binding style but an alternative which employs
    no binding.

BINDINGS
    Part 5 of the ISO 9075 SQL Standard, which sets out the standard for embedded
    SQL.

BIT
    [1] Short for binary digit. A minimal computer storage unit which can have a
    value of either 0 or 1. Four bits make a nibble. Eight bits make a byte (in
    SQL terms: an octet).

    [2] An SQL Standard term. The SQL-92 BIT data type is used to store bit data.

    [3] An ODBC term. The ODBC BIT data type is not the same thing as the standard
    BIT data type.

BIT STRING
    A sequence of bit values. All Columns defined as BIT have bit strings; all
    literals of the form B'nnnn' or X'nnnn' are bit strings.

BIT_LENGTH
    The size of a string, expressed as a number of bits.

BLOB
    [1] Also spelled BLOb. See: BINARY LARGE OBJECT.

    [2] Obsolete. An abbreviation for "basic large object".

BLOCK
    [1] Synonym for page.

    [2] An Oracle term. A sequence of statements. See: COMPOUND STATEMENT.

BLOCK CURSOR
    An ODBC term. When multiple-row fetches are possible, with SQLExtendedFetch
    for instance, the Cursor is said to be a block Cursor.

BNF
    Abbreviation for Backus-Naur Form. A formal syntax notation method. Basic
    rules are: if a list is in braces you must choose one and only one of the
    items in the list; anything within brackets is optional; and ::= means
    "expands to some simpler token (closer to the Terminal)". For example:

    ::

        <set function> ::= COUNT(*)
                           | { AVG | MAX | MIN | SUM | COUNT }
                             ( [ALL | DISTINCT] <scalar expression> )

    Meaning: either you can use COUNT(*), or you can use any one of AVG or MAX or
    MIN or SUM or COUNT followed by "(" followed optionally by either ALL or
    DISTINCT followed by <scalar expression> (which is presumably defined
    elsewhere) followed by ")".

BOOLEAN
    [1] Having to do with George Boole, English mathematician, 1815 - 1864.

    [2] (Of an operation) AND/OR/NOT.

    [3] (Of a value) TRUE/FALSE. Mr Boole himself preferred two-valued logic, so
    strictly speaking a three-valued logic is not Boolean.

    [4] An SQL3 data type defined by the keyword BOOLEAN. There are three values
    possible: TRUE, FALSE and UNKNOWN.

BOUND COLUMN
    A Column specified in a select list (or -- rarely -- in a VALUES statement),
    and therefore a Column of a result set. This Column becomes "bound" when it is
    associated with a host language variable's address. That happens when the
    ARD's item descriptor area's SQL_DESC_DATA_POINTER is set to a non-zero value
    (an address value) by a CLI function such as SQLSetDescField or SQLBindCol.
    Thus, a bound Column's value is going to an "output parameter" as seen from
    the DBMS, and when we fetch we are fetching bound Columns into bound targets.

BRACKETED COMMENT
    An SQL3 novelty. A comment within an SQL statement which begins with ``/*`` and
    ends with ``*/``, as in C.

BSI
    Abbreviation for British Standards Institute.

BUFFER
    [1] (noun) An area allocated by the host language application program, which
    it shares with the DBMS, especially for transfer of parameter data.

    [2] (verb) what a DBMS does when it keeps internal copies of result sets or
    temporary data without immediately returning it to the host language
    application.

BUILT-IN DATA TYPE
    See: PREDEFINED DATA TYPE.

BUILT-IN FUNCTION
    A function whose description is part of the SQL language definition -- e.g.:
    AVG (a set function) or LOWER (a scalar function). In SQL-92 all functions are
    built-in. In C, and soon in SQL3, functions are usually part of a system- or
    user-defined library.

BYTE
    Not an official term. The preferred word to refer to a group of 8 bits is
    "octet". In some rather old contexts e.g. the DEC PDP-10, a "byte" could be 6
    or 7 bits.

C
-

C
    A host language, recognized by the SQL Standard. (The variant, C++, is
    unofficial.)

C DATA TYPE
    A basic descriptor of a scalar variable used in a C host language program. In
    SQL circles one would specifically say "C data type" to ensure there is no
    confusion with an SQL data type of the same name (e.g.: the SQL data type
    INTEGER is always 32-bit signed, the C data type integer (i.e.: int) may be
    short or may be unsigned).

CALCULATED FIELD
    An MS-Access term. See: VIRTUAL COLUMN.

CALL STATEMENT
    An SQL3 statement of the form "CALL [name] [parameter list]" where [name]
    refers to a routine, possibly a function, consisting of either more SQL
    statements or a routine in a host language. The idea of SQL invoking non-SQL
    is an SQL3 innovation.

CANDIDATE KEY
    A key which may be used to identify a single row. There may be several
    candidate keys defined for a Base table, one of which may be the "preferred
    candidate key". The preferred candidate key may be explicitly designated as
    the "primary key". Thus, a candidate key is definable by any UNIQUE or PRIMARY
    KEY Constraint. A candidate key which is not a primary key is an "alternate
    key".

CANDIDATE ROW
    (Obsolete) an outer row, whose values are visible in the inner SELECT of a
    correlated subquery.

CAPITAL LETTER
    See: UPPER CASE LETTER.

CARDINAL NUMBER
    The number of elements in a set: 0,1,2,3,... Represented by an unsigned
    integer. (Technically: differs from a Natural Number since in some definitions
    the natural numbers do not include zero, and may refer to anything.)

CARDINALITY
    The number of occurrences in any sort of repetition, for example the number of
    elements of a set. Thus a C array defined as "x[4]" has a cardinality of 4.
    Thus a Table with zero rows (an empty Table) has a cardinality of 0. Thus the
    cardinality of any row is the number of Fields. Thus the cardinality of an
    array is the number of elements.

CARTESIAN
    A Cartesian product of the sets A and B is the set of all ordered pairs (a,b)
    where a is a member of A and b is a member of B. In database terms: a
    Cartesian product joins all rows in Table A with all rows in Table B:

    ::

        A   B   Cartesian Product
        a1  b1  a1,b1
        a2  b2  a1,b2
                a2,b1
                a2,b2

    Cartesian products are useful for explanation, but when we see an operation
    which "goes Cartesian" we usually criticize the optimizer. Also known as a
    cross join.

CASCADE
    Continue an UPDATE or DELETE on the next level due to foreign key clauses, or
    continue a DROP due to a CASCADE clause. Domino effect. Cascading always goes
    from top to underlying (just as a water cascade always goes downhill);
    therefore it is the reverse of inheritance.

CASE
    [1] In SQL, an expression of the form "CASE ... END" which returns a scalar
    value depending on the result of evaluation of one or more search conditions
    within the expression.

    [2] An abbreviation for Computer Aided Software Engineering.

    [3] The form of a letter: upper case = capital letter, lower case = small
    letter.

CASE SENSITIVE
    A comparison is "case sensitive" if lower case strings do not equal upper case
    strings, e.g.: 'ABC' <> 'abc'. The opposite is "case insensitive". The
    Standard defines case insensitivity only in the context of regular
    identifiers, where it says that lower case letters should be converted to
    upper case before comparison or storage. For other cases, the DBMS decides
    whether a case-insensitive Collation should be used, in which case it should
    define: (a) whether only simple Latin letters are affected, (b) whether the
    conversion is from lower to upper or vice versa, (b) whether it is possible
    for the default Collation to be case insensitive.

CAST
    To change a value's data type, if possible without altering its physical
    representation. Thus, CAST ('1994-01-01' AS DATE) is equivalent to DATE
    '1994-01-01'.

CATALOG
    [1] An SQL Standard term. The level in the SQL Object-qualifier hierarchy
    between Cluster and Schema.

    [2] A non-standard term. The metadata Tables which describe an entire
    database. The simplest possible database structure has only one Cluster, one
    Catalog and one Schema; when this is the case the terms "Catalog" and
    "database" and "Schema" may be used interchangeably. A detailed form of a
    Catalog is a DATA DICTIONARY.

CATALOG FUNCTION
    A CLI term. Any of the CLI functions which implicitly accesses metadata in an
    implementation-dependent way (probably by selecting from INFORMATION_SCHEMA)
    and returns a result set. Examples: SQLColumns, SQLTablePrivileges,
    SQLForeignKeys.

CBEMA
    Abbreviation for Computer and Business Machine Manufacturers' Association,
    which manages some of the affairs of the X3 database standards committee.

CHAIN
    [1] (Identifier chain) A sequence of identifiers linked by periods See also:
    QUALIFIER.

    [2] An SQL3 keyword. An indication, in a ROLLBACK or COMMIT statement, that
    the next transaction should begin with some characteristics carried over from
    the previous one.

CHAR
    Abbreviation for CHARACTER (data type).

CHARACTER
    [1] A Unicode term. Anything listed in the ISO 10646 standard document.
    Examples of characters are: letters of the alphabet, digits, punctuation
    marks, ideographs, control (non-graphic) characters.

    [2] An SQL keyword. One of the basic data types. May be abbreviated: CHAR.
    CHAR fields contain letters, digits, etc. An example of a CHAR literal is
    'John Doe'.

CHARACTER LARGE OBJECT
    See: CLOB.

CHARACTER REPERTOIRE
    See: REPERTOIRE.

CHARACTER SET
    [1] An SQL Standard term. A repertoire plus a Form-of-use plus an encoding.
    Example: take the Latin alphabet (that is the repertoire) ... decide that each
    character will be represented by one octet (that is the Form-of-use) ...
    specify 65 (hex 41) is the code for 'A', 66 is the code for 'B', etc. (that is
    the encoding) ... you have a Character set. Character sets are Schema Objects,
    they can be made with CREATE CHARACTER SET and destroyed with DROP CHARACTER
    SET.

    [2] = character repertoire. (Since Form-of-use and encoding don't matter
    unless strings are being input or output, when discussing pure DBMS contexts
    the terms "Character set" and "character repertoire" may be used
    interchangeably.) We frown.

CHARACTER STRING RETRIEVAL
    A CLI term. Several CLI routines use this parameter trio: ``CHAR *target``,
    ``SMALLINT target_octet_length``, ``SMALLINT *returned_octet_length`` (parameter names
    may differ but if you see these parameter types in this sequence it means some
    sort of character string retrieval is happening). Rules for the most common
    case are:

    If (target_octet_length<=0) error: invalid string or buffer length

    If (returned_octet_length is not a null pointer)
    ``*returned_octet_length = strlen(character-string);``
    Copy character-string and null-terminator ("\0") to target.

    If target too short, truncate and add warning-string data, right
    truncation.

    There are some exceptions, see the first CLI chapter.

CHECK CONSTRAINT
    A Constraint which is based on a clause that begins with the word CHECK.
    Example: ALTER TABLE Table_1 ADD CONSTRAINT ch CHECK (c1>7) adds a CHECK
    Constraint for Table_1; all values in Column c1 must either be greater than 7,
    or be NULL.

CHECK OPTION
    A flag setting caused by the WITH CHECK OPTION clause of a View definition.
    When it is true, any updates made to the View must be compatible with any
    search conditions in the View definition. For example: "CREATE VIEW v AS
    SELECT * FROM Table_1 WHERE col_1 > 5 WITH CHECK OPTION ... INSERT INTO v
    VALUES (4)" is a violation of the View's check option.

CHECKPOINT
    A moment during a transaction when the DBMS dumps all updates made so far, but
    does not fully commit -- i.e.: Cursors are not closed. See also: SAVEPOINT.

CLASS
    [1] A mathematical term. A synonym for set, but one uses the word class only
    when the members of the set have some close relation with each other.

    [2] An object oriented term. See: UDT.

    [3] An SQL Standard term. In the 5-octet status code (SQLSTATE) which the DBMS
    returns as diagnostic information, the first 2 octets are the "class" (the
    next 3 octets are the "subclass"). Commonly encountered classes are '00'
    (successful completion), '01' (warning), '02' (no data), etc.

CLASS ORIGIN
    An SQL Standard term. The origin of the class is the documentary authority
    which defines the meaning of the class. Example: class 'IM' has class origin =
    'ODBC 3.0'; class '42' has class origin = 'ISO 9075'.

CLAUSE
    Part of an SQL statement, beginning with a word which in English is usually a
    preposition or a relative conjunction. For example:  in the SQL statement
    "DELETE FROM Table_1 WHERE S1 = 5", FROM Table_1 and WHERE S1 = 5 are clauses.
    Also: where we would usually see a comma or break in English. For example:
    "ALTER TABLE Table_1 ADD CONSTRAINT C CHECK (C1 > 5)", where one can feel the
    break before the word CHECK, so CHECK (C1 > 5) is a clause.

CLI
    SQL Standard term. Call Level Interface. The SQL Standard ("ANSI/ISO/IEC
    9075-3:1995 Database Language SQL - Call Level Interface") specifies a CLI
    very similar to ODBC, which preceded it. A CLI is one way to interface SQL
    with a host language and is called a "binding style" (the other important
    binding style is embedded sql). See also: API, SAG/CLI.

CLID
    Abbreviation for: Common language-independent datatype. An inchoate ISO
    standard. The idea is that inter-language data passing will be more reliable
    if representations have commonly-agreed-upon descriptions.

CLIENT/SERVER
    A two-tier database system architecture, with (usually) one "server"
    machine/program and (usually) multiple "client" machines/programs. Sometimes
    client and server functionality is combined in the same database engine, with
    no separation which is apparent to outside observers. The server is the
    bartender, the clients are the waitresspersons/waiterpersons, the application
    programs are the tavern patrons.

CLOB
    Character Large Object. A data type, much like CHAR, but also analogous to
    BLOB. There are some restrictions on operations which can be performed with
    CLOBs. The intent of the specification is that, to compensate, CLOBs can be
    relatively large.

CLOSE
    [1] To release a result set when no further fetching is required, done in
    embedded SQL with "CLOSE <Cursor>" and in the CLI with SQLCloseCursor.

    [2] A non-standard term. To "close a file" is to declare to the operating
    system that the program no longer requires the handles and buffers associated
    with the file. By extension, "close a database" means to close all database
    files.

CLOSURE
    A mathematical term. A set has the property of closure for an operation, if an
    operation on any member of the set will produce a member of the same set.
    Example: addition has closure for the set of integers because adding two
    integers always results in an integer; however, division does not have closure
    for integers because dividing 3 by 2 results in 1.5 which is not an integer.

CLUSTER
    [1] A standard but little-used term. The top level of the SQL Object hierarchy
    (the next level is the Catalog level, then comes the Schema level, then
    Objects such as Tables or Domains). Most DBMSs do not support multiple
    Clusters, therefore there is usually no need to use [cluster.] as a Catalog
    qualifier. As an analogy to the hierarchy, we suggest you think of a
    personal-computer hierarchy:  the top [Cluster] level is the computer itself,
    the next [Catalog] level is the drive or drives, the next [directory] level is
    the Schema and then comes the [Table] level with individual files.

    [2] A non-standard term. An area of physical storage. Some DBMSs can store
    multiple Tables in the same file or disk volume, and it is part of the
    database designer's job to specify which Tables should be thus collocated.
    Careful clustering helps performance.

    [3] A non-standard term. A "cluster key" is the key which a DBMS optionally
    uses to order the rows within a Table, when storing in files.

COALESCE
    An SQL scalar operator. The expression COALESCE(a,b,c) returns a if a is not
    NULL, else returns b if b is not NULL, else returns c if c is not NULL, else
    returns NULL.

COBOL
    A computer language which the SQL Standard defines as a host language.

CODE PAGE
    A Windows term. A mapping between numbers (usually 8-bit octets unless the
    code page is Unicode) and characters. See also: FORM-OF-USE.

CODING
    See: ENCODING.

COERCIBILITY
    An SQL Standard term, always used concerning Collations. If a character
    string's Collation can be changed, it is coercible.

COLLATION
    [1] An operation which puts character strings in order.

    [2] An object in a database which describes Collation.

    [3] = collating sequence.

COLLATING SEQUENCE
    A specification of the character string comparison rules for sorting or
    conditional-expression purposes. Typically a collating sequence will be based
    on alphabetical order, and typically the alphabet will be Latin, but there are
    many variants and special considerations. A default collating sequence exists
    for every character repertoire.

COLLECTION
    An SQL3 data type. A collection contains multiple values of the same
    underlying data type. In the SQL3 Standard, all collections are arrays.

COLUMN
    [1] An Object described within a CREATE TABLE statement, to represent the
    vertical component of a Table (the horizontal component is a row).

    [2] An instance of such an Object within a row, in which case it may also be
    called a "Field" or "attribute". Note: this term does not come from set
    theory, but is commonly used.

COLUMN CONSTRAINT
    A type of Table Constraint which is originally defined within the
    Column-definition area, e.g.: "CREATE TABLE Table_1 (col_1 INTEGER NOT NULL)"
    contains a NOT NULL Column Constraint.

COLUMN FUNCTION
    (Obsolete) See: SET FUNCTION.

COLUMN INTEGRITY RULE
    Derivation from the relational-theory phrase "attribute integrity rule", which
    is (changing the word attribute to Column): there is an implicit Constraint on
    every Column, that every Column value is a value which exists in the Column's
    Domain.

COLUMN REFERENCE
    A reference -- using an identifier -- to a Column of a Table. The select list
    "[SELECT] 5, CAST(:x AS INT), t_detail" contains a literal, then a parameter
    in an expression, then a Column reference.

COMMA LIST
    Not an SQL Standard term. Used in some textbooks for the lists, usually of
    indefinite size and enclosed within parentheses, most often of Columns --
    e.g.: "CREATE VIEW V (v1,v2,v3,v4) ...". The BNF is (<item> [,item ...]) but
    shorter forms exist.

COMMAND
    See: SQL STATEMENT IDENTIFIER.

COMMENT
    [1] A part of a statement which has no effect on execution, used usually for
    program documentation. The standard SQL-92 comment is marked by -- and
    continues until the end of the line:

    ::

        INSERT INTO T_1 SELECT column1 FROM T_2; -- simple comment

    With SQL3 one can begin a comment with ``/*`` and end with ``*/``, the C style:

    ::

        INSERT INTO T_1 /* bracketed comment */ SELECT column1 FROM T_2;

    See also: SIMPLE COMMENT, BRACKETED COMMENT.

    [2] A non-standard SQL verb for putting remarks in INFORMATION_SCHEMA Views.
    For instance, IBM's DB2 allows COMMENT ON TABLE x IS 'this is a table';.

COMMIT
    An SQL statement which makes changes permanent. In the CLI the same purpose is
    usually accomplished with SQLEndTran (or the transaction can be in committed
    automatically, see Automatic Commit). Sometimes the word "commit" (lower case)
    refers to the act of flushing to the data files without closing the Cursors;
    this is the operating-system meaning of "commit" rather than the SQL
    definition, and a better word would be "save". Once you COMMIT, you cannot
    ROLLBACK.

COMMUTATIVE OPERATOR
    An operator which doesn't care about the order of the operands, e.g.: A+B is
    the same as B+A. Note that A-B is not the same as B-A, so - is not
    commutative.

COMP-OP
    An SQL Standard term. An abbreviation for "comparison operator".

COMPARISON
    A comparison operator is one of: = > >= < <= <>. The combination <expression>
    <comparison operator> <expression> constitutes a comparison predicate (the
    standard term) or simply "comparison" (the popular term). An operation which
    takes two scalar values -- or two row values if the DBMS is full SQL -- and
    returns true or false or unknown. Example: the comparison predicate "5 > 2" is
    true. See also: PREDICATE.

COMPATIBLE
    An SQL Standard term referring to data types. Two data types are compatible if
    they are mutually assignable and their descriptors include the same data type
    name. Example: a CHARACTER and CHARACTER VARYING are compatible, unless they
    are of different repertoires (in which case they are not mutually assignable).

COMPILATION UNIT
    An SQL Standard term. A series of executable statements. These are associated
    with the client Module while it is executing.

COMPILE
    To parse a series of statements in a host language, and produce object code
    for the computer processor. Current DBMSs are not compilers; they only produce
    tokens which must be interpreted by a runtime software module. However, some
    sources (including Microsoft) will use the word "compile" as a synonym for
    "prepare".

COMPLETION CONDITION
    Any SQL statement or CLI function will either fail due to some error or
    problem ("exception"), or execute till "completion". In the latter case, a
    "completion condition" will be in a function return and/or in a status code.
    There are three classes of completion condition: success (class = 00), success
    with information i.e.: warning (class = 01), no data (class = 02). Usually the
    term "completion condition" is not used unless there is a warning involved.

COMPLEXITY
    (Kolmogorov's rule) The complexity of a sequence is the length of the shortest
    computer program which can be used to print it out.

COMPONENT
    [1] (Of a UDT) Either an attribute or operation -- but loosely, "component"
    may refer to attributes only.

    [2] (In general) Anything which belongs to a larger structure, for example a
    years value is a component of a datetime, Domains are components of Schemas,
    operands are components of expressions and Constraint attributes are
    components of Constraint descriptors.

COMPONENT
    [1] An Object/Relational term. (Of a UDT) Either an attribute or a method.

    [2] A general term. A Table is a component of a Schema, a Schema is a
    component of a Catalog, etc.

COMPOSITE KEY
    A key which contains more than one Column. Also known as a concatenated key,
    or multi-value key. Opposite of: simple key.

COMPOUND STATEMENT
    A sequence of statements which can be treated as a unit -- what in Pascal
    would be enclosed in "begin ... end", what in C would be enclosed in braces.
    In SQL3 (PSM) a compound statement has a local scope and a degree of
    atomicity.

CONCATENATION
    Catena is the Latin word for chain. When we concatenate, we are chaining
    together. Or actually: stringing together, because the operands of a
    concatenation operation must be strings. The concatenation operator is ||. For
    arrays, there is a built-in function: CONCATENATE.

CONCISE CODE
    A CLI term. A representation of data types using single numbers: 1 = CHAR, 2 =
    NUMERIC, 3 = DECIMAL, etc. Each variant of the datetime and interval data
    types is represented by a different value (for example 103 = INTERVAL DAY and
    104 = INTERVAL HOUR); in that respect a concise code value differs from an SQL
    data type code value. See also: SQL DATA TYPE CODE.

CONCISE FUNCTION
    [1] A CLI term. A function which accesses a descriptor "implicitly"; the first
    parameter is a statement handle rather than the descriptor handle. Examples:
    SQLBindCol, SQLBindParameter.

    [2] An ODBC term. A CLI function which acts on more than one descriptor field.
    Examples: SQLGetDescRec, SQLSetDescRec.

CONCURRENCY
    From the Latin "concurrere" -- to run together. When two applications, or two
    instances of the same application, are connected to the same database, they
    are concurrent. Conflict is possible; it can be regulated with an optimistic
    control (e.g.: timestamping) or a pessimistic control (e.g.: locking).

CONDITION
    [1] A logical term. Given two statements p,q: the formulations "p implies q"
    or "p is necessary for q to be true" express conditional relations.

    [2] The contents of the ON clause of a join. See also: SEARCH CONDITION.

    [3] The result of an SQL operation which is returned to the application via
    the Diagnostics Area. See also: EXCEPTION CONDITION, COMPLETION CONDITION,
    STATUS RECORD.

CONDITIONAL EXPRESSION
    (In the writings of C.J.Date) a synonym for the standard term search
    condition.

CONDITIONAL VALUE EXPRESSION
    One of: CASE, NULLIF, COALESCE.

CONDITION HANDLING
    A PSM term. A system whereby exception or completion conditions can be linked
    with procedures for handling them. See: HANDLER.

CONDITION INFORMATION ITEM
    An SQL Standard term, but little used. A multiple-occurrence detail record in
    a diagnostics area. We have preferred the term: status record.

CONFORMANCE LEVEL
    [1] An ODBC term. Describes how completely a driver conforms to the API
    requirement (core, level 1, level 2).

    [2] An SQL term. Describes how completely an implementation conforms to the
    SQL Standard (entry, intermediate, full, core, enhanced).

CONNECTION
    [1] (data source connection) what you get when you execute the CONNECT
    statement, or (with the CLI) call SQLConnect. Standardly a Connection is
    between a client and a server, but it could be between an application program
    and a DBMS.

    [2] (database connection) an opening of a database; a binding between a
    program and a database; the pipe of the linkage is the connection.

    [3] (allocated connection) see dbc. See also: SESSION.

CONNECTION BROWSING
    An ODBC term. Looking for a data source, either by querying the ODBC data
    manager or by making calls to the operating system.

CONNECTION HANDLE
    See: hdbc.

CONNECTION STATEMENT
    Also SQL-Connection statement. SQL Standard term. One of: CONNECT, DISCONNECT,
    SET CONNECTION.

CONSISTENCY
    [1] If you do the same thing twice with the same original data, you get the
    same result. Consistency is one of the ACID transaction features. See also:
    DETERMINISTIC.

    [2] Two fields in a desc are consistent if they don't imply contradictory
    things. For example, for a NUMERIC data type, PRECISION=3 and SCALE=2 would be
    "consistent" -- but SCALE=100 would not be consistent because NUMERIC(3,100)
    is an illegal definition.

CONSTANT
    See: LITERAL.

CONSTRAINT
    [1] An SQL Standard term. An Object within a Schema, which contains a
    description of a CHECK clause, or a foreign key or a unique key (especially a
    primary key). If the Constraint condition is FALSE, that is an attempted
    Constraint violation. Usually the SQL statement causing the violation
    (UPDATE/INSERT/DELETE) fails; there are some other options for referential
    Constraints.

    [2] A non-standard term. Any rule which is seen by the DBMS programmer as a
    description of the database, rather than a procedural definition.

CONSTRAINT MODE
    When the Constraint must be checked for violation. One of: IMMEDIATE or
    DEFERRABLE.

CONSTRUCTED TYPE
    An SQL Standard term. One of the categories of data types (the others are
    predefined data type and UDT). Constructed types' specifications include one
    of the keywords: ARRAY, REF or ROW.

CONSTRUCTOR FUNCTION
    An Object/Relational term. A function associated with a structured
    instantiable UDT, which returns a value equal to a new instance of type UDT.
    The DBMS implicitly creates a constructor when the UDT is created, thus:
    "CREATE FUNCTION <UDT name> () RETURNS <UDT name> ... RETURN V" -- where V is
    a value of type UDT, containing the default value for every UDT attribute (as
    gotten by the attributes' observer functions). So the constructor function for
    a UDT named STUDENT would simply be STUDENT(), and its returned type would be
    STUDENT.

CONTAINMENT
    The Standard uses the words "directly contains" for the special case where a
    part of an SQL statement (such as a clause) includes another part (such as an
    expression), at the same level. Thus, in "SELECT * FROM Table_1 WHERE col1 =
    (SELECT col2 FROM Table_2);", the WHERE clause "directly contains" the Column
    reference col1, but the Column reference col2 is in a subquery and is
    therefore not directly contained in the WHERE clause.

CONTROL DECLARATION
    Also SQL-control declaration. A PSM term. One of: a condition declaration, a
    handler declaration or a variable declaration, within an SQL Module.

CONTROL STATEMENT
    Also SQL-control statement.

    [1] An SQL3 term. One of: CALL, RETURN.

    [2] A PSM term. Since the point of PSM is the addition of control statements,
    there are several statement types here: "compound", "case", "if", "iterate",
    "leave", "loop", "while","repeat", "for", and "assignment" statements.

CONVERT
    [1] Change one data type to another, either implicitly or (via the CAST
    operator) explicitly.

    [2] An SQL scalar operator which changes the form of use of a char string.

CORE ODBC
    The ODBC 3.0 specification includes a description of "core ODBC", which is
    reasonably close to what we know as "the standard CLI". Full ODBC would also
    include many non-core extended features, none of which are standard.

CORE SQL
    The SQL3 Standard specification includes a description of "Core SQL", a subset
    of SQL3 that (it is expected) will be adhered to by more DBMS vendors than can
    support the whole thing.

CORRELATED SUBQUERY
    A subquery which contains a reference to a Column in an outer Table -- e.g.:
    the statement "SELECT * FROM T_1 WHERE EXISTS (SELECT * FROM T_2 WHERE
    T_1.Column=T_2.Column)" contains a correlated subquery, in which the Column
    reference T_1.Column refers to a Column in T_1, and T_1 is in the FROM clause
    of the outer query.

CORRELATION NAME
    [1] An alternate Table name, occurring in a FROM clause within a SELECT
    statement, whose scope is the scope of the SELECT statement. One uses
    correlation names as shorthand, and to prevent ambiguity in self joins.

    [2] An alternate Table name, occurring in a Trigger definition.

CORRESPONDING
    Having the same name. The SQL clause [CORRESPONDING [BY (Column list)]
    modifies the UNION, EXCEPT and INTERSECT operators.

CORRIGENDUM
    Also: Technical Corrigendum. From the Latin for "thing which must be
    corrected". If errors or ambiguities are discovered in an ANSI document after
    it has been published, a supplementary bulletin comes out. For SQL-92 there
    were three Corrigenda, the latest (which supersedes the previous ones) is
    known as Corrigendum #3.

COUNT
    One of the SQL set functions, used for tallying.

CROSS JOIN
    Cartesian join. The SQL expression "a CROSS JOIN b" is equivalent to "a
    [INNER|LEFT|RIGHT|FULL] JOIN b ON <predicate>" where a and b are Tables and
    the predicate is true.

CURRENT
    As of the time that an SQL statement is executing. CURRENT is used as a prefix
    for SQL datetime niladic functions (CURRENT_DATE, CURRENT_TIME,
    CURRENT_TIMESTAMP) and for the user who connected (CURRENT_USER) and for the
    naming path for routines (CURRENT_PATH).

CURRENT ROW
    Where the Cursor is at, within a result set. For instance, when you FETCH
    [NEXT] for the first time, the Cursor will be positioned on the next row,
    which is 1. (Row numbering within result sets starts at 1.) The concept
    matters when you use UPDATE|DELETE ... WHERE CURRENT OF <Cursor>.

CURRENT_USER
    An SQL niladic character string function, which returns the authorization
    identifier of the Module. If the Module has no authorization identifier, then
    CURRENT_USER = SESSION_USER i.e.: the authorization identifier of the user who
    logged on during the CONNECT. See also: SYSTEM_USER.

CURSOR
    A named linkage to a result set, used by a host language program to navigate
    row-by-row. Generally: one creates a result set with a query, which is
    associated with a Cursor, then fetches through the Cursor one row at a time.
    With a scroll Cursor one can fetch particular rows, using an absolute or
    relative index to the result set.

CYCLE
    [1] An SQL Standard term. An instance of a recursion.

    [2] See: REFERENTIAL CYCLE.

D
-

DARWEN, HUGH
    Database expert. Co-author (with C.J.Date) of an SQL book. Member of SQL
    committee.

DATA
    Also SQL-data. The plural of the Latin word datum ("a given"). Anything stored
    in a database. All the data in a database's Tables, but not the metadata.
    Effectively: same as Database.

DATA BANK
    Obsolete. See: DATABASE.

DATA CHANGE STATEMENT
    Also SQL-data change statement. One of: INSERT, UPDATE, DELETE. In this book
    we have preferred the term "data change statement" to the somewhat ambiguous
    looking "update statement".

DATA CONTROL LANGUAGE
    Also DCL. Non-standard term. The subset of the SQL language which consists of
    those statements that affect Privileges. To wit: GRANT, REVOKE. Properly, the
    phrase should be "access control" (to avoid confusion with SQL3's new control
    statements).

DATA DEFINITION LANGUAGE
    Also DDL. Non-standard term. The subset of SQL syntax containing the SQL
    statements which create or destroy Objects (other than Privileges) and
    descriptions of Objects. That is: CREATE, DROP, ALTER.

DATA DICTIONARY
    [1] In SQL: The set of all descriptions of all Objects in a Cluster (users,
    Catalogs, Schemas, Tables, Columns, Domains, Privileges, etc.). Some of the
    information in the data dictionary is visible in INFORMATION_SCHEMA Views.
    Until SQL-92 came and declared "Cluster" to be the top database-hierarchy
    level, a "data dictionary" was the same thing as a "Catalog" -- this meaning
    is still common.

    [2] Outside SQL: a list of data-related names, policies and procedures needed
    for administration. Some authorities distinguish between "metadata inside the
    database" (the INFORMATION_SCHEMA) and "metadata in the environment as a
    whole" (the data dictionary).

DATA ELEMENT
    Non-standard term. See: ATTRIBUTE.

DATA ENVIRONMENT COMMANDS
    Rarely-used non-standard term. The CONNECT and DISCONNECT statements. See
    also: CONNECTION STATEMENT.

DATA EXCEPTION
    A class of exceptions which are raised as a result of a problem with the data,
    for example "character not in repertoire" or division by zero".

DATA MANIPULATION LANGUAGE
    Also DML. Non-standard term. The subset of SQL syntax containing the SQL
    statements which manipulate data -- e.g.: INSERT, UPDATE, DELETE, SELECT.

DATA MANIPULATION STATEMENT
    An SQL Standard term. An SQL statement which accesses or changes rows, to wit:
    the data change statements (INSERT, UPDATE, DELETE); the query statements
    (SELECT, TABLE, VALUES) and their Cursor overhead (OPEN, FETCH, CLOSE). In
    SQL3, FREE LOCATOR and HOLD LOCATOR are also data manipulation statements.

DATA REPOSITORY
    See: REPOSITORY.

DATA SOURCE
    An ODBC term. The combination of location plus DBMS plus database -- the thing
    one connects to. In many cases, the data source is simply the database.

DATA TYPE
    An SQL Standard term. A description of a set of values, which determines what
    representations and operations (if any) are legal. For example: "TIME WITH
    TIME ZONE", "CHAR(14) CHARACTER SET ASCII_FULL", "UDT_1". A full data type
    description includes: data type name plus size plus (for character data types)
    Character set and Collation. However, to many people the word "CHAR" alone
    defines a data type; the rest of the description (size plus Character set plus
    Collation) is regarded as distinct from the data type. See also: DECLARED
    TYPE, PREDEFINED DATA TYPE, UDT.

DATA TYPE CODE
    Also SQL Data Type Code. A representation of data types using single numbers,
    e.g.: 1 = CHAR, 2 = NUMERIC, 3 = DECIMAL, etc. Each variant of the datetime
    and interval data types is represented by the same value, and a separate
    "subtype" code would be required to differentiate the variants. For example
    for INTERVAL DAY the SQL data type code value = 10 and the subtype = 3 while
    for INTERVAL HOUR the SQL data type code value = 10 and the subtype = 4. In
    that respect a SQL Data Type Code value differs from a concise code value. The
    ODBC term for SQL Data Type Code is "verbose code". See also: CONCISE CODE.

DATA TYPE SPECIFIER
    A data type name preceding a literal or host variable in an SQL statement. For
    example, the SQL statement "SELECT * FROM Table_1 WHERE DATE_Column = DATE
    '1992-01-01'" contains a data type specifier: the word DATE. See also:
    INTERVAL QUALIFIER.

DATA-AT-EXECUTION
    An ODBC term, adjectivally attached to either the word "Column" or the word
    "parameter". Refers to values which cannot be determined at prepare time, but
    which will be known at execution time.

DATABASE
    [1] The collection of Catalogs, Schemas, Tables, Constraints, Domains, rows,
    etc. i.e.: the data plus the description of the data.

    [2] A Cluster.

    [3] An ODBC term. "a discrete collection of data in a DBMS. Also a DBMS".

    [4] An MS-Access term. All objects related to a subject, including tables,
    forms and modules.

DATABASE ENGINE
    All parts of the DBMS (parser, optimizer, file reader, etc.) which work on the
    database -- usually excluding those parts of the DBMS (precompiler, installer)
    which have a peripheral role. See also: DRIVER.

DATABASE MANAGEMENT SYSTEM
    See: DBMS.

DATE
    [1] C.J. (Chris) Date writes books on relational databases.

    [2] An SQL data type for representing year+month+day.

DATETIME
    [1] One of the standard SQL data types: DATE, TIME, TIMESTAMP.

    [2] A Microsoft SQL Server data type, see TIMESTAMP.

DATETIME_INTERVAL_CODE
    See: SUBTYPE.

DAY-TIME INTERVAL
    An interval which includes one, some, or all of these fields: DAY, HOUR,
    MINUTE, SECOND. See also: YEAR-MONTH INTERVAL.

DB2
    See: IBM.

DBA
    Abbreviation for Database Administrator.

DBASE
    Official spelling is dBASE. Trademark of Inprise Corp. A non-SQL ISAM DBMS
    which (according to the vendor) was "relational" and which was popular on
    microcomputers in an age which (thank goodness) is now past.

DBC
    A CLI term. A structured area which is created by the
    SQLAllocHandle(SQL_HANDLE_DBC,...) function. The dbc is contained in an env.
    The dbc can contain several stmts. The dbc stores information about a
    connection. The standard term is actually "SQL-connection" but in examples the
    Standard uses the abbreviation dbc; throughout this book we have preferred to
    use the term dbc because it appears less confusing to us. The CLI functions
    which reference a dbc use a handle; we call a dbc handle a hdbc. Possibly  at
    one time dbc stood for "database connection" or "DBMS connection", but that is
    no longer the case.

DBL
    An abbreviation for a subgroup of ISO, as in "the Database Languages
    Rapporteur Group of ISO/IEC JTC1/SC21/WG3". Informally: the international
    equivalent of ANSI X3H2.

DBMS
    Not an SQL Standard term. Short for Database Management System. For this book
    we use DBMS for "an SQL product from a known vendor" or merely "whatever your
    application is connecting via and to" -- wherever the details don't matter.
    Often we use the word DBMS where the formal word would be "implementation".

DBMS-BASED DRIVER
    An ODBC term. A driver that accesses data by calling a database engine. As
    opposed to a File-Based Driver, which contains a database engine.

DBSSG
    Abbreviation for Database Systems Study Group.

DCL
    See: DATA CONTROL LANGUAGE.

DDL
    See: DATA DEFINITION LANGUAGE.

DEADLOCK
    A concurrency problem. When Job #1 is waiting for Job #2 to release a lock on
    record X, but Job #2 is waiting for Job #1 to release a lock on record Y, each
    job must in theory wait forever.
    DEALLOCATE

    [1] An embedded-SQL keyword. DEALLOCATE DESCRIPTOR is the reverse of ALLOCATE
    DESCRIPTOR.

    [2] An SQL Standard term. One can "deallocate" any resource. Simpler synonyms
    are "free" or (our own preference) "destroy".

DECIMAL
    Having to do with tens or with tenths.

    [1] A number with a number base (radix) = 10, what mathematicians call
    "denary", as opposed to "binary" (based on the number 2) or "hexadecimal"
    (based on the number 16).

    [2] An exact numeric data type which has a user-specified decimal precision
    and optional scale. An example of a decimal literal is: 15.77. See also:
    NUMERIC.

DECIMALDIGITS
    A parameter in the CLI functions SQLBindParameter and SQLDescribeCol, where it
    indicates the number of digits after the decimal point -- the scale if a
    numeric data type, the fractional precision if a temporal data type.

DECLARATION
    [1] A Module definition may contain a "temporary Table declaration". It looks
    like a CREATE TABLE statement, but the temporary Table declaration is
    considered to be a data statement (like SELECT), not a data definition
    statement.

    [2] In the function call "a(b,c,d)", b and c and d are "parameter
    declarations".

    [3] An embedded SQL term, referring to any statements which the precompiler
    should see but not execute, e.g.: DECLARE CURSOR, SET NAMES ARE (the Character
    set declaration), or the variable definitions between BEGIN DECLARE SECTION
    and END DECLARE SECTION.

DECLARED TYPE
    [1] (Of a Column, parameter or variable) The data type that is "declared" in
    the definition, for example in CREATE TABLE Table_1 (x INTEGER) the declared
    type of x is INTEGER.

    [2] (Of an expression) The data type that is implied by SQL's syntax rules.
    For example: in WHERE y = DATE '1994-04-04' + INTERVAL '1' DAY, the literal
    has a declared type of DATE. For an example that shows the distinction between
    declared type and most specific type, see: MOST SPECIFIC TYPE.

    [3] (Common incorrect definition) "Of an expression denoting a value, the
    unique data type that is common to every value that might result from
    evaluation of that expression" -- usually no such data type exists.

DECOMPOSE
    To break up Tables as part of the normalization process. For example: if we
    have a Table "Countries (country_name ... PRIMARY KEY, monarch ..., heir
    ...)", and we determine that one of the rules of normalization is violated
    (specifically: see THIRD NORMAL FORM), then we would split into two Tables,
    with one referencing the other. See also: NORMALIZATION.

DEFAULT
    [1] A system-defined mode or value which is in effect unless the user
    explicitly requests otherwise.

    [2] A clause in Column- or Domain-definition, with a scalar value. Example:
    ALTER TABLE Table_1 ADD COLUMN c DEFAULT NULL;. (For the PSM specification,
    there can be a default clause for variables too.)

    [3] A clause which is taken to exist in a statement if no specification exists
    to the contrary; usually the Standard puts this as "If <x> is not specified,
    then <y> is implicit".

DEFERRABLE
    (Of a Constraint) Capable of being deferred. The opposite of "IMMEDIATE".

DEFERRED
    (Of a Constraint) For which checking is postponed until either a COMMIT
    happens, or until SET CONSTRAINTS ... IMMEDIATE happens.

DEFERRED PARAMETER
    A "parameter" is a value which is input from the application to the DBMS. If
    the parameter value is established before execution, it's an "immediate
    parameter". If the parameter value is established during execution, it's a
    "deferred parameter". Deferred parameters are signalled by SQL_NEED_DATA. The
    SQLParamData function is usually needed.

DEFINE
    [1] (In a database) Add to the database structure using a CREATE or GRANT
    statement. The standard term "Schema definition" reflects this meaning.

    [2] (In relational theory) imply, as in "since we can derive the value of b
    from the value of a, we say that a defines b". See also: FUNCTIONAL
    DEPENDENCY.

DEFINITION_SCHEMA
    The INFORMATION_SCHEMA Tables are actually, in the official description, Views
    which are derived from Base tables in DEFINITION_SCHEMA. But you never access
    these Base tables, so this is an academic issue.

DEGREE
    [1] A relational term. A Table with 3 Columns has a degree of 3.

    [2] An SQL3 term. The number of attributes in a user-defined type.

DELETE
    One of SQL's Database Manipulation Language verbs (the others are INSERT and
    UPDATE). When a row is deleted, it is removed from a Table.

DELETE RULE
    The part of a Constraint clause that begins with the words "ON DELETE ...".
    This specifies referential action on a foreign key if a primary key is
    deleted.

DELIMITED TEXT FILE
    A disk file containing a representation of a Table, in which rows and Columns
    are separated from each other with special character markers ("delimiters").
    If the Columns are separated with commas, it is a "comma delimited [text]
    file".

DELIMITED IDENTIFIER
    Also "quoted identifier". An identifier which is enclosed in double quotes ("
    "). Unlike regular identifiers, delimited identifiers may match keywords or
    may contain special characters. Case is significant: "A" and "a" are not the
    same.

DELIMITER TOKEN
    Any of: 'character literal', the quoted string which is part of
    date/time/timestamp/interval literals, "a delimited identifier", a special
    character, or <> or >= or <= or || or .. or [ or ]. A delimiter is a token
    which need not be surrounded by separators, thus "A <> B" and "A<>B" are the
    same expression. The ANSI definition contains unclearnesses; it may be that
    certain other characters are delimiters too. See also: SEPARATOR.

DELPHI
    A popular implementation of Pascal, vended by Inprise Corp.

DENORMALIZE
    Break the normalization rules deliberately, in an attempt to gain speed or
    save space.

DEPRECATED
    [1] A term used in the Standard for syntax that was okay in an earlier
    version, but which they wish you'd stop using -- and maybe in the next version
    you won't be able to use it at all. An example is the use of ordinals in ORDER
    BY clauses.

    [2] (referring to an English word) Disapproved.

DEREFERENCE
    An SQL3 operation. To take a REF value and return the value which it refers
    to.

DERIVED COLUMN
    An entry in a select list, other than "*". Thus, in "SELECT 1 + 1 AS
    one_plus_one FROM INFORMATION_SCHEMA.LANGUAGES;", the sole expression in the
    select list -- the value expression "1 + 1" with the AS clause -- is the
    derived Column, and the derived Column name is one_plus_one.

DERIVED TABLE
    [1] A Table whose definition and contents come from another Table due to an
    SQL query statement, such as SELECT. All result sets are in theory "derived
    Tables", but we usually reserve the term "derived Table" for Views. A
    persistent Base table is not a derived Table.

    [2] Any virtual Table which is materialized. See also: VIRTUAL TABLE.

DESC
    [1] A CLI term. Abbreviation for CLI descriptor area. This is one of the four
    types of resources (the others are env, dbc, stmt). A desc contains fields
    that describe a result set's Columns, or a statement's parameters. See also:
    APD, ARD, IPD, IRD.

    [2] contraction for descending.

DESCENDING
    Going down. In a descending sort sequence, the number 4 comes after the number
    5, and the letter 'G' comes after 'K'. Opposite is ascending. In SQL one must
    use the short form: DESC.

DESCRIBE
    In embedded SQL, DESCRIBE is used to retrieve information (name, size, scale,
    etc.) about parameters or result set Columns. The equivalent CLI functions are
    SQLGetDescRec, SQLDescribeCol and their analogs.

DESCRIPTOR
    [1] See: DESCRIPTOR AREA.

    [2] (In a database) a structure which is maintained by the DBMS for an Object,
    values in which are changed by Schema Statements, and often selectable via the
    Views of INFORMATION_SCHEMA. Examples: "Table descriptor", "Domain
    descriptor".

DESCRIPTOR AREA
    [1] An embedded SQL term. A structure defined in a host language (the SQLDA),
    or available to the host language via a handle, which contains information
    about the Columns of a result set (data type, size, name, etc.).

    [2] A CLI term. See: DESC.

DESCRIPTOR INDEX
    Within a descriptor area there is a multiple-occurrence structure (the item
    descriptor area, which occurs once per Column). If we refer to the Nth
    occurrence of the descriptor's item descriptor area, then N is the descriptor
    index.

DESCRIPTOR RECORD
    An ODBC term. Within a descriptor area, there are n descriptor records (where
    n = the value of the descriptor area's COUNT). The fields in a descriptor
    record are name, length, scale, etc. One descriptor record describes either
    one dynamic parameter specification or one select-list Column. In this book we
    use the standard term "Item Descriptor Area" instead of "Descriptor Record",
    but acknowledge that SQLGetDescRec obviously is short for Get Descriptor
    Record.

DESKTOP DATABASE
    A database which is accessed from a personal computer, without recourse to a
    server on a different machine. The term is sometimes used pejoratively.

DETAIL
    A report line containing information from a single row -- as opposed to a
    "summary" or "group" line.

DETERMINISTIC
    (Of a query) Guaranteed to produce the same result every time, if the database
    is the same. Factors which might break determinism, and thereby cause
    "possibly non-deterministic" queries, include the implementation-dependent
    behaviour that the Standard allows for time zones and padded character
    strings. A difference in row order is not significant. Queries used in
    integrity Constraints must be deterministic.

DIAGNOSTIC RECORD
    An ODBC term. See: STATUS RECORD.

DIAGNOSTICS AREA
    Structured information concerning the execution of the last SQL statement or
    CLI function call. Fields in the diagnostics area are available to the
    application via a GET DIAGNOSTICS statement (embedded SQL) or via a
    SQLGetDiagField/SQLGetDiagRec function (CLI SQL). The diagnostics area
    contains some header fields (e.g.: the count of conditions and the return
    code) and zero or more status records. Information in the status records might
    be useful if an exception or completion condition occurred.

DIAGNOSTICS AREA LIMIT
    The maximum number of status records which may exist within one diagnostics
    area. It is possible to change the limit with a SET statement. The limit can
    never be less than 1.

DIAGNOSTICS STATEMENT
    A general name for: GET DIAGNOSTICS.

DICTIONARY
    [1] An authoritative source for determining a Collation.

    [2] See: DATA DICTIONARY.

DIFFERENCE
    A relational operation. See: EXCEPT.

DIGIT
    One of: 0123456789. The term "digit" may be used for non-decimal numbers, but
    see also: BIT, HEXIT.

DIN
    [MISSING ENTRY]

DIRECT
    Without stopovers. If we have a type hierarchy where t1 is a subtype of t2 and
    t2 is a subtype of t3, then t1 is a subtype of t3 but it is not a direct
    subtype of t3. Also, a "direct" subtype is always a "proper" subtype.

DIRECT SQL
    A binding style. If you type an SQL statement on your keyboard and results
    come back on the screen, you are using direct SQL. There is some relaxation of
    the formal SQL rules, which are generally meant to apply to SQL statements
    interacting with a host language program. The Standard uses the term Direct
    Invocation of SQL.

DIRTY READ
    A reading of data which another transaction has updated or inserted, but not
    committed. Dirty read can occur if the transaction isolation level is "read
    uncommitted".

DISCONNECT
    An SQL verb, the reverse of CONNECT. Terminates a session.

DISJOINT
    Two sets are disjoint if they have no elements in common. The mathematical
    term "mutually exclusive" is sometimes used.

DISPLACEMENT
    The distance between a local time zone and UTC, expressed as a number of hours
    and minutes, between -13:00 and +12:59.

DISTINCT
    [1] Adhering to Cantor's definition of a set, in that all members are
    distinguishable from one another.

    [2] An SQL keyword, which causes redundant duplicates (if there are any) to be
    discarded or ignored. In the statement "SELECT DISTINCT Column1,Column2 FROM
    Table_1;", the word DISTINCT is sometimes called the "distinct set
    quantifier". See also: DUPLICATE, UNIQUE.

DISTINCT PREDICATE
    An SQL3 term. The predicate "x IS DISTINCT FROM y" is FALSE if x and y are
    duplicates, otherwise it is TRUE.

DISTINCT TYPE
    An Object/Relational term. A UDT which is not a structured type. A distinct
    type is made with "CREATE TYPE AS <predefined data type> ... FINAL"; it is
    (perhaps) always instantiable; it (perhaps) has methods; it cannot be a
    subtype or supertype of anything except itself. Distinct types are supposed to
    be useful when "senseless" assignments/comparisons are avoidable through
    strict type checking.

DISTRIBUTIVE
    An arithmetic term. What happens to one member of the class, happens to all
    members. Since A*(B+C) is the same as A*B+A*C, multiplication is distributive
    over addition. Addition is not distributive over multiplication, because
    A+(B*C) <> A+B * A+C.

DLL
    A Windows term. A library which is loaded at runtime.

DML
    See: DATA MANIPULATION LANGUAGE.

DOCUMENTATION_SCHEMA
    An SQL3 term. A set of implementation-defined Base tables which any user can
    SELECT from, containing information about the DBMS's workings (presumably --
    this part of the Standard is unfinished).

DOMAIN
    [1] A set of values, all of which have the same data type. For instance the
    Domain of cardinal numbers includes those integers which are >= 0. (Notice
    that this would be an infinitely large set; if we are talking about database
    contents, see: COLUMN). In standard SQL, we use Domains in the way we would
    use simple macros in C, when we define Columns.

    [2] (In set theory only) the set of values of the first coordinate (i.e.: the
    first Column) of a binary relation.

DORMANT
    (Of a Connection or session) Not current. If you are already connected, and
    you connect again, you end up with two Connections. The old one is dormant,
    the new one is current. Nothing happens on a dormant Connection unless you
    revive it: by disconnecting the current Connection, by using SET CONNECTION or
    by performing an operation which causes an implicit SET CONNECTION.

DOUBLE PRECISION
    One of the three approximate numeric data types. The others are REAL and
    FLOAT.

DOUBLE QUOTE
    A special character used to enclose delimited identifiers. Although the
    Unicode name for " is "quotation mark", in SQL the word is double quote and is
    not the same as quote. See also: QUOTE, ".

DRIVER
    [1] An ODBC term. A software component, generally a DLL, which mediates
    between an application and a DBMS. The application is linked to Microsoft's
    Driver Manager library. The application calls an ODBC function, the Driver
    Manager receives it and passes it on to the driver, the driver calls the DBMS
    engine. (In a multi-tier environment there would be yet another pass-on, from
    the DBMS "client" to the "server".) The engine does the work, and results
    meander back via the same components till they reach the application.

    [2] An SQL Standard term. "A component of the client that is responsible for
    communicating with one or more SQL-servers as a driver." Process details are
    implementation-defined, the simplest scenario would be: the application calls
    a single library that does all the DBMS work.

DRIVER MANAGER
    An ODBC term. A DLL supplied by Microsoft, and included in many host language
    compiler packages from Microsoft and other vendors. An ODBC application
    program calls the driver manager, which calls a driver. The "management" that
    the program does is mainly: deciding what driver to call, buffering connection
    data and performing some elementary translations so that drivers of different
    versions will appear similar to the application.

DRIVER SETUP DLL
    An ODBC term. A DLL supplied by a DBMS vendor (it might be within the vendor's
    driver), which is needed for installing a driver.

DROP
    Destroy. Remove an Object (a Table or Column or Constraint or Domain or
    Trigger or Collation or Translation or Character set) from the Catalog. If the
    Object is a Table, delete all rows in the Table too.

DUPLICATE
    An SQL Standard term. Two values are duplicates if they are equal or if they
    are both NULL. See also: DISTINCT, EQUAL.

DURABILITY
    Resistance of a committed transaction's record to change or destruction after
    the COMMIT. Enhanced by flushing disk buffers, and by logging. Durability is
    one of the four ACID transaction features.

DYADIC
    An SQL Standard term. A dyadic operator has two operands, and so is
    distinguished from niladic, monadic and triadic operators. Multiplication (*)
    is dyadic.

DYNAMIC CONSTRAINT
    An Assertion or integrity Constraint, for which both before and after images
    can be addressed, or temporary values. See also: TRIGGER.

DYNAMIC CURSOR
    ODBC term. Scrollable updatable Cursor. When a row is updated, the new data
    will be accessible via the Cursor. With a static Cursor, the data would appear
    to be unchanged.

DYNAMIC PARAMETER
    CLI term. In the SQL statement "SELECT * FROM Table_1 WHERE col_1 = ? AND
    col_2 = ?;" there are two dynamic parameters, represented by question marks in
    the input string. A dynamic parameter is an input to the DBMS. An output from
    the DBMS is a target.

DYNAMIC PARAMETER SPECIFICATION
    [1] CLI term. The question mark ? which signifies that a dynamic parameter is
    to be substituted for a literal at execute time.

    [2] Embedded SQL term. The :<host-variable-name>.
    A dynamic parameter is an input parameter.

DYNAMIC PARAMETER VALUE
    The application program's copy of a dynamic parameter.

DYNAMIC SQL
    With dynamic SQL, the application can find out at runtime what the description
    of parameters and result set Columns is. In the CLI, this capability depends
    on the application's capability of accessing "desc" resources (the descriptor
    areas). The opposite is: static SQL.

DYNAMIC STATEMENT
    Also: dynamic SQL statement. An SQL statement (in a Module or embedded SQL)
    which maintains resources for use in dynamic SQL. The dynamic statements are:
    EXECUTE, EXECUTE IMMEDIATE, ALLOCATE DESCRIPTOR, DEALLOCATE DESCRIPTOR, GET
    DESCRIPTOR, SET DESCRIPTOR, PREPARE, DEALLOCATE PREPARE, DESCRIBE INPUT,
    DESCRIBE OUTPUT.

DYNASET
    An MS-Access term. A result set produced via an updatable query.

E
-

EBCDIC
    Abbreviation for Extended Binary Coded Decimal Interchange Code.An 8-bit
    Character set used on larger IBM computers.

ELEMENT
    An SQL Standard term. An occurrence in an array, addressed with
    "array-name[N]".

ELEVATOR SEEK
    An operating system term. Travelling through a disk's physical locations in
    the manner of an elevator, instead of jumping backward or forward for each
    request.

EMBEDDED SQL
    SQL statements which are placed within host language programs in a way which
    makes it appear that they are part of the language, and which require a
    precompilation step to be converted to API calls. Described in ISO 9075-5
    "SQL/Bindings".

EMPTY SET
    A set-theory term. A set which has no members. That is, a set whose
    cardinality is zero.

ENCAPSULATION
    An object-orientation term. The placing of activities and data together in a
    black box. Attributes in ADTs are encapsulated, so they are accessible only
    via observer functions, if at all.

ENCODING
    Also (occasionally) coding. A convention for character machine representation.
    For instance we may agree that the encoding for 'A' is one octet, with bits =
    01000001. The set of encodings for the characters of a repertoire is the
    Form-Of-Use. A map of encodings for a one-octet Character set is a Codepage.

ENCOMPASSING TRANSACTION
    It is possible that the DBMS environment is part of some wider environment
    (for example a network, or an automated cash drawer). In such a case a
    "COMMIT" by the DBMS alone could be premature (for example because the rest of
    the network must also commit, or because the drawer is stuck). In that case
    the COMMIT is the responsibility of the larger system. The activities carried
    out by the larger system are the "encompassing transaction".

ENTITY
    The concept which we try to reflect with the database construct, "Table". For
    instance, there are such things as "Customers" and "Sales". In a "Customers"
    Table, each customer is an occurrence of the entity.

ENTRY SQL
    The lowest level of SQL-92 Standard conformance (below Intermediate SQL).

ENV
    Also Allocated SQL-Environment. A CLI term. A structured area created by the
    SQLAllocHandle (SQL_HANDLE_ENV,...) function. An env can contain several dbcs,
    which in turn can contain several stmts. The CLI functions which reference
    envs always use a handle. We call the handle of an env a henv. The full
    standard terms are "Allocated SQL-Environment" and "handle of allocated
    SQL-Environment", but programs and constants -- including those programs and
    constants which appear in the Standard -- are abbreviated: env and henv.

ENVIRONMENT
    [1] The global situation which applies for all database connections. For
    example, the environment might be: the Windows95 operating system, with no
    network.

    [2] Whatever the DBMS allocates when a program calls SQLAllocEnv, presumably
    an area of memory with session-specific information.

    [3] The Cluster plus the Connections.

ENVIRONMENT ATTRIBUTE
    There is only one standard environment attribute: see NULL TERMINATION.

ENVIRONMENT HANDLE
    See: HENV.

EQUAL
    Two values are equal if they have the same measure. For numeric values:
    subtracting one value from the other yields zero -- not necessarily with the
    same representation e.g.: 5.0 = 5, and not necessarily exactly, e.g.: 1.0E+1
    might equal 10.00000001. For character values: the Collation decides -- e.g.:
    'ABC' might equal 'ABC '. A NULL is not equal to a NULL (the equality
    comparison would return UNKNOWN), but see also: DUPLICATE.

EQUIJOIN
    Also spelled equi-join. A join which matches Columns using the = operator.
    This is by far the most common type of join.

EQUIVALENT
    The Standard uses equivalent to mean "corresponding" (for example lower-case u
    is equivalent to upper-case U), or "having the same meaning" (for example the
    expression ``A /* comment */ + B`` is equivalent to the expression ``A + B``), or
    even "equal" -- but in that case we would prefer to use the exact word: equal.
    "Equivalent" is the correct word to use when comparing identifiers.

ERROR
    Not a formally defined word, but as a general rule the word "error" refers to
    mistakes detected by the DBMS in its input -- a syntax error in the SQL
    statement, an array subscript out of range, an attempt to retrieve a NULL
    without using an indicator, etc. See also: EXCEPTION CONDITION.

ESCAPE
    [1] An ODBC term, designating a gob of non-standard syntax which is placed
    within an SQL statement inside {braces}.

    [2] A replacement factor in a LIKE or SIMILAR pattern.

    [3] An obsolete IBM term, referring to the double quote character which is
    placed at the start or end of a delimited identifier.

ESCAPE SEQUENCE
    [1] (in standard C) A backslash followed by a code value or a mnemonic, used
    for hard-to-read or extended characters. Examples: \" \0 \t.

    [2] (in a variable-encoding Character set) a state-change signal to the effect
    that the meaning of following characters is to be interpreted according to
    different rules than were used for preceding characters.

ESTABLISH
    [1] The SQLConnect function "establishes a connection". It is possible for a
    dbc (standard term: SQL-connection) to be unestablished if it has been
    allocated with the SQLAllocHandle(SQL_HANDLE_CONNECT,...) function but no
    SQLConnect has been done, or SQLDisconnect has been done.

    [2] The SQLFetch or SQLFetchScroll function "establishes a current row" by
    positioning the Cursor over a particular row in the result set.

EVENT
    A general term. An action which may be detected by some system which then
    generates a further action. For example: in Windows, a mouse click is an
    event. For example: a Trigger event.

EXACT NUMERIC
    One of: SMALLINT, INTEGER, DECIMAL, NUMERIC -- the numeric data types which
    are not "approximate numeric".

EXCEPT
    Merge two Tables, excluding rows which have values in common. See also:
    INTERSECT, UNION.

EXCEPTION CONDITION
    [1] An SQL Standard term. An exception is a syntax error, attempted access
    violation, data incompatibility or environmental problem -- usually we'd just
    call it an "error". SQL statements or CLI functions which fail to execute will
    return an "exception condition" as part of the diagnostics. A mere warning or
    no-data situation is not an exception -- see: COMPLETION CONDITION. Usually an
    operation which returns an exception condition has no effect -- it merely
    fails, but that's not in the definition.

    [2] In non-SQL contexts an "exception condition" is either an error or a
    warning.

EXCEPTION STATEMENT
    The declarative statement in embedded SQL that begins with the words EXEC SQL
    WHENEVER.

EXCLUSIVE
    A type of lock. If Job #1 has an exclusive lock on row X, then Job #2 can
    neither read nor write row X. Compare: SHARED LOCK.

EXECUTE
    [1] Run. Do. Go. Execution is the activity of an SQL statement, or statement
    within a host language, which is distinct from preparation i.e.: from
    precompilation / preparation / binding.

    [2] A CLI term. Call the SQLExecute function.

EXISTS
    One of the SQL predicates, almost always associated with a correlated
    subquery, as in "SELECT * FROM T_1 WHERE EXISTS (SELECT * FROM T_2 WHERE
    T_2.col = T_1.col);" where the predicate means "such that there is a row of
    Table T_2 whose col Column equals a col Column in any row of T_1".

EXPLAIN
    Describe an access plan. This is a non-standard optional command in some
    DBMSs. For example, EXPLAIN might deliver the information that a query will be
    executed using an index.

EXPLICIT
    Right there in black and white. Specified. The reverse is implicit.

EXPLICITLY-ALLOCATED DESC
    An ODBC term. See: USER DESC.

EXPONENT
    A number within an approximate numeric literal, possibly signed, preceded by
    the letter E. The number indicates what power to raise 10 to. For example,
    15E+00 is "15 times 10 to the zeroth power (i.e.: 1)". See also: MANTISSA.

EXPONENTIAL NOTATION
    Also known as scientific notation or floating-point notation. In its standard
    form, exponential notation represents approximate numeric literals using: an
    optional sign, a decimal mantissa (usually between 1 and 10), the letter E, an
    optional sign and a decimal exponent. For example, the number 123 is
    represented in exponential notation as 1.230000E+02.

EXPORT
    To ship data out of the database. Usually this involves taking an entire
    Table's contents and converting it into a file format that can be read by
    non-DBMS programs.

EXPRESSION
    Any combination of operators and operands, yielding a value that can in turn
    be used as an operand. Sometimes expressions are classified by what they
    return ("value expressions" "Table expressions"), in non-standard texts
    expressions are classified by what they contain ("conditional expressions"
    "group expressions").

EXTENSION
    A feature which is not in the SQL Standard, generally requiring additional
    language. For example, indexes.

EXTERNAL ROUTINE
    [1] External here means "outside the (SQL) environment". A routine written in
    a host language which is called from SQL.

    [2] In any non-SQL context, an "external routine" is simply a routine in a
    different program.

EXTRACT
    An SQL integer function, which returns a component of a datetime. For example,
    EXTRACT (YEAR FROM DATE '1994-01-12') is equivalent to the integer 1994.

EXTREME FUNCTION
    Infrequent term. The aggregate functions MIN() and MAX() are collectively
    referred to as the "extreme" functions.

F
-

FALSE
    [1] In two-valued logic, a logical value which is not TRUE.

    [2] In SQL (which often uses three-valued logic), a logical value which is
    neither TRUE nor UNKNOWN. See also: LOGIC.

FAMILY
    An Object/Relational term.

    [1] Just as a human family may be thought of as the set of people who have (or
    are) a common ancestor, a "type family" is the set of all types with a common
    supertype. Since predefined data types or distinct types cannot have proper
    supertypes, the only type families which can have more than one member are
    structured types. For an illustration of a type family, see: MINIMAL COMMON
    SUPERTYPE. See also: HIERARCHY, STRUCTURED TYPE, MAXIMAL SUPERTYPE.

    [2] Similarly to [1], a "Table family" is the set of all Tables with a common
    supertable.

FEATURE
    A capability of a particular DBMS, to handle a certain data type or operation.
    With the CLI, one can find out about some DBMS features by calling the
    SQLGetInfo function. With SQL3, the features are in the SQL_FEATURES
    INFORMATION_SCHEMA View. For example, feature E091-5 is: can this DBMS do the
    SUM set function?

FETCH
    The act of taking a row, or a set of rows, out of a result set. The data and
    status indicators generally are transferred to buffers allocated by the host
    language program.

FETCH ORIENTATION
    One of: NEXT, FIRST, LAST, PRIOR, ABSOLUTE, RELATIVE. A modifier that tells
    the DBMS which direction to go in the result set, before fetching a row.
    Embedded SQL example: "EXEC SQL FETCH ABSOLUTE 55 Cursor_name INTO
    :host_variable :indicator_parameter;".

FETCH TARGET
    The host variable and indicator variable which will receive the value of a
    Column in a result, when FETCH happens. Fetch target addresses are specified
    in the ARD.

FIELD
    [1] An instance of a Column in a row of a Table. Thus, a scalar value which is
    taken from a row and Column intersection.

    [2] Loosely: a Column.

    [3] An SQL3 term. A (Field name, data type) pair within a row type. The Field
    value is the data type value.

FILE
    A persistent-storage object which often is physical (on disk), and often has a
    one-to-one relationship with an SQL persistent Base table. We reject the C
    standard definition: a sequence of bytes including disk files, pipelines and
    console input.

FILE-BASED DRIVER
    An ODBC term. A driver that contains a database engine instead of calling a
    database engine (as a "DBMS-based driver" does). Do not be misled by the word
    "file-based"; all ODBC drivers must ultimately perform file input/output at
    some level.

FILE SERVER
    An architecture, having to do with computers in a network. A file server does
    file operations (open/read/write/close etc.) but does not do higher-level
    database management operations (SELECT/UPDATE/etc.). Thus it differs from a
    client/server architecture. Because some people believe that file servers are
    relatively inefficient, they are becoming less common.

FINAL
    Part of a UDT definition. If a UDT is "final", it may not be a proper
    supertype -- that is, it may not be the object of an UNDER clause in a CREATE
    TYPE statement.

FIPS
    Abbreviation for [United States] Federal Information Processing Standard. The
    main document is FIPS PUB 127-2, Database Language SQL (30 pages), which
    helpfully specifies what the US government wants for some feature that the
    SQL-92 Standard says are "implementor-defined". The document is also issued as
    a package along with the SQL-92 Standard (ANSI X3.135-1992).

FIRE
    Execute (the SQL statements in a Trigger). The phrase "fire a Trigger" is
    popular but we do not use it in this book because the standard phrase is
    "activate a Trigger".

FIRST NORMAL FORM
    A relational term. A Table is in first normal form if there are no
    multiple-occurrence Columns. Since standard SQL-92 does not allow array
    definitions, this is fairly easy to achieve. See also: NORMALIZATION.

FIXED-LENGTH ENCODING
    An encoding for a Character set, in which all characters require the same
    amount of computer storage space -- generally one octet for the 8-bit sets for
    European languages, but two octets (16 bits) for the most popular
    manifestation of Unicode. See also: CODE PAGE, FORM-OF-USE, ISO 8859-X,
    VARIABLE-LENGTH ENCODING.

FIXED-LENGTH STRING TYPE
    CHAR and BIT Columns are "fixed-length" if they are not explicitly defined as
    VARYING. Insertions into such Columns are always padded on the right, so that
    every Column value has the same length. All character string literals and bit
    string literals are fixed-length.

FLAGGER
    A feature or utility provided by the DBMS vendor, which helps application
    programmers identify SQL language which is not standard, or which depends on
    implementation-specific language extensions. One way of doing this is to
    direct the precompiler to put marks in the embedded SQL source code program.

FLOAT
    One of the three approximate-numeric data types (the others are REAL and
    DOUBLE PRECISION).

FOLD
    A scalar function used on character strings to change case. The two fold
    functions in SQL are UPPER and LOWER. The two fold functions in ODBC are UCASE
    and LCASE.

FOR
    A PSM term. A keyword which introduces a "for statement", which takes the
    form: [<label> :] FOR <loop variable name> AS [Cursor details] <Cursor
    specification> DO <SQL statement list> END FOR [<ending label>]. See also:
    REPEAT, LOOP, WHILE.

FOREIGN KEY
    A set of Columns in a Base table, corresponding to some unique key. The
    foreign key is said to "reference" the unique key. Values in foreign key
    Columns must match values in referenced Columns. Usually the foreign key and
    unique key are in different Tables, and usually the unique key is a primary
    key.

FORM-OF-USE
    An encoding for a string of characters. In the western world most Forms-Of-Use
    are eight-bit or sixteen-bit fixed-length encodings. In Asia some Forms-Of-Use
    are variable-length encodings. An example of a Form-Of-Use is: the Windows
    code page. See also: ENCODING, CODE PAGE, ISO 8859-X, UNICODE, FIXED-LENGTH
    ENCODING, VARIABLE-LENGTH ENCODING, REPERTOIRE. Technical Note: Because a
    variable-length encoding may include escape characters which in effect cause
    the encoding method to change within a string, we define Form-Of-Use as an
    encoding for a string.

FORMAT RULE
    A rule about the structure and composition of tokens in an SQL statement. For
    example: "CREAT TABL Table_1 (x CHAR(5)" violates format rules. On the other
    hand: "CREATE TABLE Table_1 (x CHAR(0))" is cleanly formatted; however, it
    breaks a syntax rule. See also: SYNTAX RULE.

FORTRAN
    A language which can be used as a host language for SQL.

FORWARD-ONLY CURSOR
    A Cursor that can only go forward, i.e.: that supports "FETCH NEXT" operations
    but not "FETCH LAST", "FETCH ABSOLUTE", etc., as a scroll Cursor does.

FRACTIONAL PRECISION
    In a TIME or a TIMESTAMP or an INTERVAL which includes a SECOND field, the
    number of positions after the decimal point which indicate the fraction of a
    second. See also: SCALE, DECIMALDIGITS.

FREE
    [1] A CLI term. Tell the DBMS that a resource (env or dbc or stmt or desc) is
    no longer needed, usually via a call to SQLFreeHandle.

    [2] An SQL3 keyword. With FREE LOCATOR, for a BLOB, CLOB, NCLOB, ARRAY or UDT,
    we can cancel the association between a locator variable and its value.

FROM CLAUSE
    The word FROM followed by one or more Table references. For example this
    SELECT statement contains a FROM clause: "SELECT * FROM Table_1;". In the
    Standard, the term "FROM clause" is used only in the context of SELECT (not
    DELETE) statements.

FULL OUTER JOIN
    An outer join which fills in for non-matching values on both the left and the
    right. For example: if Table A has {1,3,5} and Table B has {1,2,3} then the
    full outer join of A and B has { 1 1, NULL 2, 3 3, 5 NULL}. See also: OUTER
    JOIN.

FULL SQL
    One of the levels of conformance of standard SQL-92, above Entry and
    Intermediate. An implementation which claims "full SQL conformance" is making
    a big claim.

FULL-TABLE SCAN
    If the DBMS must read every row in the Table and check whether the individual
    row matches a search condition, it's doing a full-Table scan. With big Tables
    this may be less efficient than alternatives such as indexed or hashed lookup.
    If the reading is from beginning to end (as it usually is) then a full-Table
    scan is synonymous with sequential search.

FUNCTION
    [1] A CLI term. A procedure, callable from a host language program, which
    returns a value. For example, all CLI functions return a 16-bit integer in
    return code.

    [2] An SQL-92 term. An operator which returns a single value, classified
    according to the number of operands (or parameters) following it: niladic
    function (no operands, e.g.: CURRENT_TIME), scalar function (one or more
    operands but from a single row, e.g.: UPPER), set function (one operand
    possibly from more than one row, e.g.: SUM). For the latter types, the word
    "function" may apply to both the operator keyword, and to the combination of
    the keyword and its (parenthesized) operands. See also: ROUTINE.

FUNCTIONAL DEPENDENCY
    A relational term.

    (Of a Column) Whose value can be derived (determined) via examination, by a
    human, of a value in another Column. Example #1: "If it's Tuesday this must be
    Belgium" (title of a movie about tourists, where one attribute -- location --
    is uniquely defined by another -- day-of-week). Example #2: "Since name =
    'Pinocchio', nose_size = 'large'". See also: NORMALIZE.

G
-

GATEWAY
    An ODBC term. A program which is called according to the CLI protocol for
    database X, and calls according to the protocol for database Y. Thus a gateway
    is middleware. An example is Micro Decisionware's "DB2 Gateway" which makes
    IBM's DB2 look accessible to SQL Server calls.

GENERAL CONSTRAINT
    Non-standard term. See: ASSERTION.

GENERAL RULE
    An SQL Standard term. A general rule specifies what is supposed to happen when
    an SQL statement executes. See also: ACCESS RULE, SYNTAX RULE.

GET DESCRIPTOR
    An embedded SQL term. A non-preparable statement which retrieves one or more
    fields from a descriptor area. Does the same job as the CLI's SQLGetDesc...
    functions. Example: "EXEC SQL GET DESCRIPTOR desc1 VALUE 1 :simple_target_spec
    = TYPE;".

GET DIAGNOSTIC
    An embedded SQL term. A non-preparable statement which retrieves one or more
    fields from a diagnostics area. Does the same job as the CLI's SQLGetDiag...
    functions. Example: "EXEC SQL GET DIAGNOSTICS :simple_target_spec =
    ROW_COUNT;".

GLOBAL
    Accessible from any Module: the scope is the SQL-session, rather than the
    Module. The term is most commonly encountered in embedded SQL and in the
    phrase "global temporary Table".

GLYPH
    A Unicode term. From the Greek "glupho": carve, write on a tablet. What a
    character looks like to a human after it is drawn or printed. As opposed to
    encoding -- what the bits are which are used to represent the character to a
    computer.

GMT
    See: GREENWICH MEAN TIME.

GRANT
    [1] An SQL verb. To give a Privilege (to a user).

    [2] Sometimes used as a synonym for the noun "Privilege"; the usage is
    somewhat inexact since not all Privileges can be explicitly granted.

GRANT OPTION
    A characteristic of a Privilege: can it be passed on to other users? If user a
    says "GRANT <Privilege> TO b WITH GRANT OPTION", then user b has the right to
    grant the Privilege to other users.

GRANTEE
    The object of a GRANT statement; the user who should receive the Privilege(s).
    Example: in the statement "GRANT SELECT ON Table_1 TO Sam;" Sam is the
    grantee.

GRANTOR
    The current user when a GRANT statement happens; the user who is granting the
    Privilege(s). Example: CONNECT ... (authorization-ID = Sally) then "GRANT
    SELECT ON Table_1 TO Sam;". Sally is the grantor.

GRANULARITY
    [1] (Of a lock) Bigness of locked area. From coarse to fine, the hierarchy
    usually is something like: "Table locking", "page locking", "row locking",
    "Column locking".

    [2] (Of a Trigger) Whether execution happens once per statement (FOR EACH
    STATEMENT), or happens once per row-change (FOR EACH ROW).

GRAPHIC
    (Of a character) Visible. Displayable. As opposed to a control character, but
    space is also a graphic character.

GRAPHIC_IRV
    See: ASCII_GRAPHIC.

GREENWICH MEAN TIME
    An obsolete standard for determining time displacement values, named after the
    Greenwich Observatory in England, longitude zero. See also: UTC.

GROUP
    A mathematical term. To combine elements of a set using a binary operator. For
    SQL the relevant operator is "duplicate", so an SQL group is formed by
    combining duplicate values.

GROUP BY CLAUSE
    A clause beginning with the words GROUP BY, used for lumping together
    duplicate values from detail rows, often for the purpose of summarizing.

GROUP FUNCTION
    Or Group-Value Function. See: SET FUNCTION.

GROUPED TABLE
    A set of rows produced by a GROUP BY clause or a HAVING clause. Each row is
    distinct, due to the definition of "group". Rows in grouped Tables may contain
    values from set functions.

GROUPED VIEW
    A View which contains an aggregate function, a GROUP BY clause or a HAVING
    clause in its definition.

GROUPING COLUMN
    A Column in a GROUP BY clause. The grouping Column is "what we group by". For
    example: if Table Table_1 has a Column c and "SELECT c FROM Table_1;" would
    produce {'A','B','A ','C',NULL,NULL} then "SELECT c,COUNT(c) FROM Table_1
    GROUP BY c;" would produce {'A' 2,'B' 1,'C' 1,NULL 2} and the grouping Column
    is c.

H
-

HANDLE
    A value, usually a 32-bit integer, which is used to refer to a resource. For
    example: ODBC has handles for environment, connection and statement. For
    example: DBMSs often store a BLOB's handle, rather than the BLOB itself, in
    the physical row of a Table file.

HANDLER
    [1] A routine which deals with exceptions. A handler is called when the SQL
    statement fails.

    [2] A PSM term. A handler is that which is declared by:

    ::

        <handler declaration> ::=
          DECLARE {CONTINUE|EXIT|UNDO} HANDLER
          FOR <condition value list>
          <handler action = SQL procedure statement>

    ... where a condition values is one of: a SQLSTATE value, a condition name,
    SQLEXCEPTION, SQLWARNING or NOT FOUND.

HASH
    A number (Often a 32-bit integer) which is derived from Column values (fields)
    employing a lossy compression algorithm. DBMSs occasionally use hashing to
    speed up access, but "indexes" are a more common mechanism.

HAVING CLAUSE
    A clause which begins with the word HAVING and contains a search condition.
    The HAVING clause is always associated with GROUP BY (although the GROUP BY
    may be implicit). The counterpart of a WHERE clause for grouped Tables.

HDBC
    A CLI term. The handle of a dbc (a connection resource). We use hdbc as an
    abbreviation for what the SQL Standard calls "handle of the SQL-connection".
    The sqlcli.h header file contains the line: ``typedef SQLINTEGER SQLHDBC /*
    connection handle */``. See: DBC.

HDESC
    A CLI term. The handle of a desc.

HENV
    A CLI term. The handle of an env. We use henv as an abbreviated substitute for
    the cumbersome SQL Standard term "handle of the allocated SQL-environment".
    The sqlcli.h header file contains the line: ``typedef SQLINTEGER SQLHENV /*
    environment handle */``. See: ENV.

HEXADECIMAL
    (Of a number) Using radix = 16 (or: number base 16). SQL numeric values are
    always decimal, but one can use hexadecimal numbers in bit or binary literals
    -- for example X'A74B'.

HEXIT
    One of: 0123456789ABCDEF. In the bit string literal X'0A', 0 and A are hexits.
    Although used by the standard, "hexit" is a rare word. Prefer "hexadecimal
    digit".

HIERARCHICAL DATABASE
    A database where all relationships between Tables are one-to-one or
    one-to-many, never many-to-many: "a servant cannot have two masters". For
    example: SALESREPS --> SALESREPS_SALES is one hierarchy and CLIENTS -->
    CLIENTS_SALES is another hierarchy, and it would be difficulty to "join"
    SALESREPS_SALES to CLIENTS_SALES. See also: RELATIONAL DATABASE.

HIERARCHY
    [1] The SQL Object hierarchy is: Cluster --> Catalog --> Schema --> Schema
    Object (Table, Domain, Constraint, etc.). See also: CLUSTER.

    [2] A "type hierarchy" or "UDT hierarchy" is a line of descent from supertypes
    to subtypes. For example, Animals to Mammals to Primates to Chimps -- Animals
    is the top of the hierarchy (the "maximal supertype"), Chimps is the bottom of
    the hierarchy (the "leaf type").

    [3] A "hierarchy option" is part of a Privilege descriptor, indicating that
    what is granted for a supertable is also granted for all subtables. See also:
    FAMILY.

HOLDABLE CURSOR
    A Cursor which remains open when the transaction is committed. This is
    abnormal; only in SQL3 may Cursors be declared as holdable.

HOST LANGUAGE
    A computer language used to write programs that interface with SQL. The
    standard host languages are: Ada, C, COBOL, Fortran, MUMPS, Pascal, PL/I.
    Other languages, such as Java and BASIC, are seen with some frequency in
    microcomputer circles. A program written in a host language is a "host
    language program". It will contain embedded SQL statements, or it will call
    SQL via a CLI.

HOST VARIABLE
    A variable defined in a host language program, which is passed (usually by
    address) to SQL. Usually the term "host variable" is used for embedded SQL
    only (for a CLI see: PARAMETER). The host variable is always preceded by a
    colon (:). An indicator may follow; the indicator is not considered part of
    the host variable. Embedded SQL snippet: "... EXEC SQL BEGIN DECLARE SECTION;
    x char[5]; EXEC SQL END DECLARE SECTION; ... EXEC SQL UPDATE Table_1 SET col =
    :x; ..." -- x is an input host variable.

HSTMT
    An unofficial abbreviation, used mostly within programs. In CLI applications
    we have a convention that h stands for handle and so hstmt is a handle of a
    stmt. So hstmt is what the SQL Standard calls "handle of the SQL statement".
    The sqlcli.h header file contains the line: ``typedef SQLINTEGER SQLHSTMT /*
    statement handle */``. See also: STMT, HDBC, HENV.

I
-

IBM
    A vendor. Makes "DB2" (short for: IBM Database 2) Universal Database, which in
    the past has had a great influence on the SQL Standard. www.ibm.com.

IDA
    See: ITEM DESCRIPTOR AREA.

IDEMPOTENT LAW
    A set theory term. "A UNION A" returns A, "A INTERSECT A" returns A.

IDENTIFIER
    An alphanumeric string by which one references an Object in SQL. Identifiers
    are subject to some restrictions -- must not be the same as a keyword, may
    contain only certain characters in certain places etc. -- so that the parser's
    job will be easier. An identifier is part of a name; no qualification is
    necessary if an identifier uniquely identifies an Object. An analogy: the name
    "Ralph Klein" refers to a person who may be referred to simply as "Ralph", but
    if there are two Ralphs in the room we would have to use the fully-qualified
    name "Ralph Klein". Here is an example of a qualified Table name which
    contains three identifiers: Catalog1.Schema1.Table1. See also: REGULAR
    IDENTIFIER, DELIMITED IDENTIFIER.

IDENTIFIER CHAIN
    A sequence of identifiers separated by periods. Usually the chain reflects
    part of the hierarchy of Objects: [Cluster.] [Catalog.] [Schema.] Schema
    Object. For Columns, the typical chain is [Table name.] Column name, or
    [Correlation name.] Column name. See also: QUALIFIER.

IDENTIFIER LENGTH
    The number of characters in an identifier. The SQL-89 standard says the
    maximum is 18. The SQL-92 and SQL3 standards say the maximum is 128. You can
    check by passing SQL_MAXIMUM_IDENTIFIER_LENGTH to the SQLGetInfo function. If
    you use non-Latin characters in identifiers, allow more than 128 octets in
    your application program buffers because characters might be 16-bit.

IDENTITY
    An operation which returns the same value as was in the input -- thus an
    identity operation on A is "A*1" or "A+0". In set theory, if you union S with
    the empty set you end up with S.

IEC
    Abbreviation for International Electrotechnical Commission.

IEF
    See: INTEGRITY ENHANCEMENT FEATURE.

IF STATEMENT
    A PSM term. An SQL conditional statement analogous to the "if" statements of C
    and Pascal. The usual format is "IF <search condition> THEN <statement list>
    END IF", or "IF <search condition> THEN <statement list> ELSE <statement list>
    END IF"; there is also provision for ELSEIF. If the search condition is TRUE,
    the THEN statement list is executed. If the search condition is FALSE or
    UNKNOWN, the ELSE statement list is executed (if any).

IMMEDIATE
    An SQL keyword. Without waiting. An EXECUTE IMMEDIATE statement both prepares
    and executes. A SET CONSTRAINTS ... IMMEDIATE statement activates all deferred
    Constraints.

IMPEDANCE MISMATCH
    A difficulty that arises when we bind SQL and host language programs, arising
    from the different rules (e.g.: SQL's use of three-valued logic) or slight
    incompatibilities in data types (e.g.: SQL's use of multiple Character sets).

IMPLEMENTATION
    [1] An SQL Standard term. A particular SQL DBMS, usually associated with a
    manufacturer and brand name and major version, in a context. For example "IBM
    DB2 as implemented on the OS/2 operating system". The Standard avoids using
    the words "DBMS", so one sometimes finds that for an official phrase -- such
    as "implementation row descriptor" -- one could substitute "DBMS row
    descriptor" and thus emphasize that we are talking about the DBMS's side of
    things, rather than the application's.

    [2] A client-server term. The implementation is both the client and the
    server, but not the application.

IMPLEMENTATION-DEFINED
    An SQL Standard term. A characteristic of an SQL DBMS left open by the
    Standard, which must be defined by the vendor, presumably in the manual. For
    example, the SQL-92 Standard says it is "implementation-defined" whether an
    SQL-Schema statement must form a separate transaction on its own. Distinguish:
    IMPLEMENTATION-DEPENDENT.

IMPLEMENTATION-DEPENDENT
    An SQL Standard term. A characteristic of an SQL DBMS left open by the
    Standard, which need not be, indeed perhaps should not be, defined by the
    vendor. For example, the SQL-92 Standard says it is "implementation-dependent"
    what the physical representation of data should look like, so you should
    regard the file format as ephemeral. Distinguish: IMPLEMENTATION-DEFINED.
    Because implementation-dependent is eight syllables, we sometimes avoid it and
    say "not specified" or "up to the vendor".

IMPLEMENTATION PARAMETER DESCRIPTOR
    Also IPD. A parameter descriptor whose information fields are set by the DBMS.
    As opposed to: APPLICATION PARAMETER DESCRIPTOR.

IMPLEMENTATION ROW DESCRIPTOR
    Also IRD. A resource, containing information about the Columns in a result
    set, as set up by the DBMS. It can be confused with the Application Row
    Descriptor which has corresponding fields; think of the distinction this way:
    the IRD describes the "bound Columns", while the ARD describes the "bound
    targets". See also: ARD.

IMPLEMENTOR
    The person or company who creates an implementation. See also: VENDOR.

IMPLICIT
    Unstated; tacit; taken as read. In the SQL statement "SELECT COUNT(*) FROM
    Table_1 HAVING COUNT(*) > 0;" there is an implicit GROUP BY. The reverse is
    EXPLICIT.

IMPORT
    To ship data into the database. Usually this involves the DBMS reading a file
    which has been produced by a non-DBMS program, and inserting in one of the
    database Tables.

IN
    An SQL keyword. An example of an IN predicate: "IN (a,b,c)" or "IN (SELECT
    Column1 FROM Table_1)".

INCLUDE
    A set-theory term. Set A is included in set B if all members of A are also
    members of B.

INDEX
    [1] A sorted set of keys and pointers, usually associated with one Column in a
    Base table, or with several Columns in the same Base table (in which case it
    may be called a "multi-Column index" or "concatenated index"). DBMSs often use
    indexes to speed up searches, but indexes are not mentioned in the official
    Standard. Alternatives are "full Table scans" and "hashes". Nowadays the usual
    plural seems to be "indexes" rather than "indices".

    [2] A CLI term. An integer which identifies an occurrence of an array For
    example, the RecordNumber parameter in the SQLGetDiagField function is
    sometimes called an index.

INDICATOR
    An integer variable defined in a host language program, whose value
    "indicates" whether the main ("data") variable is NULL, on both input and
    input. For example: the embedded SQL statement "EXEC SQL FETCH Cursor1 INTO :a
    :b;" puts a value into a (a is the data parameter) and a value in b (b is the
    indicator parameter); if the fetched value is 'x' then a gets 'x' and b gets
    0; if the fetched value is NULL then a is irrelevant and b gets -1
    (SQL_NULL_DATA). Also, in some situations, a positive indicator value is
    returned for a truncated string.

INFORMATION_SCHEMA
    The Schema that contains the Views that describe the database -- the metadata.
    For example, to find out what Domains exist, one would select from the DOMAINS
    View in INFORMATION_SCHEMA.

INFORMIX
    A vendor. Makes "Informix Universal Server". www.informix.com.

INGRES
    A vendor.

INHERIT
    Take the characteristics of what underlies. For example, a View Column
    "inherits" the data type of the underlying Base table Column. Inheritance goes
    from underlying to top, and so is the reverse of cascading.

INHERITANCE
    An Object/Relational term. A subtype inherits every component of a supertype.
    For example: if type t1 has two attributes -- t1_a and t1_b -- and we define a
    new type t2 UNDER t1, then t2 automatically has the attributes t1_a and t1_b;
    it may additionally have its own attributes (called its "non-inherited" or
    "originally-defined" attributes). SQL allows "single inheritance": although a
    type hierarchy can have indefinite length, and although a supertype may have
    many direct subtypes, a subtype may have only one direct supertype.

INITIALLY
    An SQL keyword, used in the definition of Constraints. An INITIALLY IMMEDIATE
    Constraint starts off as "a Constraint which must be checked when the SQL
    statement ends"; it may be INITIALLY DEFERRED (deferral is until COMMIT time
    or until SET CONSTRAINTS ... IMMEDIATE).

INLINE CONSTRAINT
    An Oracle term. A Constraint which is defined within parentheses.

INNER JOIN
    A type of Join which returns only values from existing rows. Inner joins are
    the normal garden variety join. See also: OUTER JOIN.

INNER TABLE
    For "a LEFT JOIN b" the inner Table is b. For "a RIGHT JOIN b" the inner Table
    is a.

INPRISE
    A vendor. Former name: Borland. Associated with Delphi and Interbase.

INPUT
    Directional adjective, thinking of the DBMS is the centre. Thus, an "input
    parameter" is a parameter for data going from the host language to the DBMS.

INSENSITIVE CURSOR
    If a Cursor is insensitive, then changes made outside the Cursor are not
    visible to the Cursor. By "changes made outside the Cursor" we mean any
    updates, other than UPDATE|DELETE ... WHERE CURRENT OF <Cursor>, which would
    affect rows currently in the Cursor or their definition. By "visible" we mean
    "seeable if we FETCH using the Cursor". If you open an insensitive Cursor,
    then FETCH with it and see X, then DELETE every row in the Table with some
    other Cursor, then FETCH with the insensitive Cursor again, you will still see
    X -- the DELETE happened but is not visible via the Cursor. See also:
    SENSITIVE, ASENSITIVE.

INSERT
    An SQL verb. We use INSERT to add a new row to a Table.

INSTALLER DLL
    An ODBC term. The ODBC administrator calls the installer DLL, which is often
    supplied by a driver vendor, in order to find out what the components are of a
    data source.

INSTANCE
    [1] A Windows term. Say you load WordPerfect twice in different windows.
    They're not the same program -- they're two copies of the same program, with
    different resource allocations, perhaps (but not necessarily) with different
    data. The two instances are "jobs", but we might reserve the word job for a
    running of WordPerfect on another computer.

    [2] An SQL Standard term. A "physical representation of a value" at a
    particular place in storage. For example, each row in a Table is one
    "instance" of a row type. An instance of a value occurs at a site.

INSTANTIABLE
    An Object/Relational term.

    (Of a structure-type UDT) Capable of being represented; not merely abstract;
    perhaps having instances. An instantiable UDT has a constructor function, may
    be used with "new" routines, and may be the UDT associated with a typed Table.

INTEGER
    [1] Exact numeric with scale zero.

    [2] An SQL predefined data type, signed, exact numeric, scale zero, precision
    implementation-defined. In most implementations precision is 31 bits and
    INTEGER values range from -2,147,483,647 (not -2,147,483,648) to
    +2,147,483,647. See also: SMALLINT, EXACT NUMERIC.

INTEGRITY
    [1] The maintenance of a consistent state despite transaction failure or
    crash.

    [2] Adherence to Constraints, especially Constraints which have to do with
    primary and foreign keys. The two general integrity rules are entity integrity
    (no primary key Column may be null) and referential integrity (no foreign key
    may reference a nonexistent key). The word "integrity" alone never means
    attribute integrity (the requirement that every Column value must be in the
    Column's Domain). See also: REFERENTIAL INTEGRITY.

INTEGRITY CONSTRAINT
    See: CONSTRAINT.

INTEGRITY ENHANCEMENT FEATURE
    Sometimes incorrectly called: integrity enhancement facility. An addition to
    the SQL-89 Standard, involving primary and foreign keys ("referential
    integrity"). Simpler integrity features, such as unique Constraints and NOT
    NULL modifiers, were already present in the SQL-86 Standard.

INTERACTIVE SQL
    See: DIRECT SQL.

INTERFACE
    [1] The routines, protocols and specifications which are needed to cross a
    boundary between subsystems, for example the CLI is the "Call Level
    Interface".

    [2] A descriptor area. The Standard refers to the APD, IPD, ARD and IRD as
    being four "types of interfaces".

    [3] An Object/Relational term. (Of a structured UDT) The set of all functions
    which include the UDT, either in the parameter declarations or as a return
    type. Example: suppose there are 50 functions (including methods). Of these,
    20 return type "UDT1", and ten others have an input parameter of type "UDT1".
    Those 30 functions together are the "interface of UDT1".

INTERMEDIATE SQL
    A level of SQL-92 conformance. An Intermediate SQL implementation can handle
    more of the SQL specification than Entry SQL, but less than Full SQL. All the
    well-known SQL-92 implementations today are Intermediate SQL.

INTERNATIONAL ORGANIZATION FOR STANDARDIZATION
    See: ISO.

INTERNATIONALIZATION
    Sometimes spelled i18n. The rules and processes which allow for different
    customs, languages or practices. SQL takes internationalization into account
    with its various Character set features; however, in standard SQL the datetime
    formats and decimal-point notations are always the same.

INTEROPERABILITY
    The likelihood that a host language program will run using two different
    DBMSs, without requiring changes to the SQL statements in it. In theory,
    interoperability should increase with adherence to standards. See also:
    PORTABLE.

INTERSECT
    Merge two Tables, accepting only rows which have values in common. See also:
    UNION, EXCEPT.

INTERVAL
    An SQL data type for representing the difference between two dates, between
    two times or between two timestamps.

INTERVAL LEADING FIELD PRECISION
    The components of an interval are called datetime "fields". The first field is
    the "leading field". The number of positions in this field is the "interval
    leading field precision". For example, in a year-to-month interval, year is
    the leading field and we would expect it to have 4 positions.

INTERVAL QUALIFIER
    One or three words, trailing an interval literal or part of an interval Column
    definition, indicating the start and end fields of the interval. One of: YEAR,
    MONTH, DAY, MINUTE, SECOND, YEAR TO MONTH, DAY TO HOUR, DAY TO MINUTE, DAY TO
    SECOND, HOUR TO MINUTE or HOUR TO SECOND. For example, in "INTERVAL '5-5' YEAR
    TO MONTH", the words "YEAR TO MONTH" are the interval qualifier.

INTRODUCER
    [1] In the Standard: an underscore preceding a Character set name.

    [2] By extension: the combination of the underscore and the Character set
    name. For example: _ASCII_FULL 'abcd' is a CHAR literal which contains an
    introducer -- that is, the literal is explicitly marked as being in the
    ASCII_FULL Character set. In SQL-92 introducers can precede either literals or
    identifiers; in SQL3 introducers may only precede literals.

    [3] The characters that signal a comment is starting, such as -- for simple
    comments or /* for bracketed comments.

INVALID
    (Of an SQL statement) Containing incorrect syntax.

    (Of a literal) Containing an illegal combination of characters.

    (Of a locator) Not referring to anything.

INVOCATION
    See: CALL STATEMENT.

IPD
    See: IMPLEMENTATION PARAMETER DESCRIPTOR.

IRD
    See: IMPLEMENTATION ROW DESCRIPTOR.

IS
    [1] An SQL operator used in predicates which test for NULL values: IS NULL or
    IS NOT NULL.

    [2] An SQL operator which permutes the result of a logical (such as a search
    condition): IS [NOT] TRUE, IS [NOT] FALSE, IS [NOT] UNKNOWN.

ISO
    Abbreviation for International Organization for Standardization. A large
    multi-function multi-country group which publishes standards. A branch of ISO
    is IEC, International Electrotechnical Commission, the group responsible for
    computer standards. Often ISO collaborates with ANSI so if there is an ANSI
    standard there is often an ISO standard which is nearly the same.

ISO 8859-X
    One of the standard 8-bit character sets. See also: ISO STANDARD CHARACTER
    SET.

ISO 9075, ISO 92, etc
    See: ISO STANDARD SQL.

ISO COMMITTEE
    Originally, the ISO group responsible for information technology was TC97
    ("technical committee 97"). After some reorganization and a merging with IEC
    this became JTC1 (presumably "joint technical committee 1"). Then Open Systems
    Interconnect (OSI) got involved, and the liaison job "Information Processing
    Transfer and Retrieval for OSI" went to SC21 ("subcommittee 21"). This in turn
    divided into subgroups, of which one was WG3 ("working group 3"). Full title:
    ISO/IEC JTC1/SC21/WG3 ("International Organization for Standardization /
    International Electrotechnical Commission / Joint Technical Committee #1 /
    Subcommittee #21 / Working Group #3".

ISO STANDARD CHARACTER SET
    There are many ISO standards relating to character sets. What we consider the
    most important ones are: ISO/IEC 646:1991. 7-bit coded Character set for
    information interchange -- see also ASCII; ISO/IEC 10646-1:1993, Information
    technology - Universal Multi-Octet Coded Character set (UCS) - Part 1:
    Architecture and Multilingual Plane -- corresponds closely to the Unicode
    Consortium's The Unicode Standard Version 2.0 (1996) -- the Standards for
    Unicode 2.0 16-bit character names and encodings; ISO 8859-x. Some matters
    having to do with collating are mentioned in ISO/IEC CD 14651, Information
    technology - International String Ordering - Method for comparing Character
    Strings.

ISO STANDARD DATE
    The relevant document is ISO 8601:1988, Data elements and interchange formats
    - Information interchange - Representation of dates and times. Summary: use
    the Gregorian calendar, represent dates and times as yyyy-mm-dd and
    hh:mm:ss.ffffff.

ISO STANDARD SQL
    Publication by ISO as an official standard. Often nearly the same as ANSI
    standard SQL, for example ISO/IEC 9075:1992 = ANSI X3.135-1992 except for a
    different foreword and normative reference.

    ## SQL-89 STANDARD: (the digits '1989' are the publication year):
    ISO/IEC 9075:1989 Database Language SQL.

    ## SQL-92 AND SQL3 STANDARDS: ISO/IEC 9075:199x, Information technology
    - Database languages comes in five parts which are actually separate
    documents: Part 1: Framework (introductory); Part 2: Foundation (this is the
    big one); Part 3: Call-Level Interface (CLI); Part 4: Persistent Stored
    Modules (PSM); Part 5: Host language bindings (for embedded SQL).

    ## RDA DOCUMENTS: ISO/IEC 9579-1:1993(E), Information Technology-Open
    Systems Interconnection-Remote Database Access, Part 1: Generic Model,
    Service, and Protocol ISO/IEC 9579-2:1993(E), Information technology-Open
    Systems Interconnection-Remote Database Access, Part 2: SQL specialization.

ISO/IEC JTC1/SC22 WG15
    The "fifteenth working group" (WG15) the "twenty-second subcommittee" (SC22)
    of the "first Joint Technical Committee" (JTC1) of ISO/IEC. JTC1 deals with
    information technology; SC is the JTC1 subcommittee which deals with
    programming languages. Member countries include Australia, Brazil, Canada,
    France, Germany, Japan, Korea, The Netherlands, the UK and the US. ISO 9579-2
    was prepared by a different subcommittee (ISO/IEC JTC1 SC21 "Open Systems
    Interconnection, Data Management and Open Distributed Processing"). ISO's web
    page is: www.iso.ch.

ISOLATION
    Two transactions work in total isolation if they have no effect on each other
    until COMMIT; but in the real world no transaction is an island. For
    concurrency purposes, SQL acknowledges four ascending levels of isolation:
    READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE. ODBC adds:
    VERSIONING. Isolation is one of the four ACID transaction features.

ITEM
    Not a formal term, but often one uses "item" for anything that might have a
    value, such as a field, attribute, variable, Column or parameter.

ITEM DESCRIPTOR AREA
    An SQL Standard term. Often abbreviated IDA. A record used by the DBMS for
    storage of information about one parameter or about one Column in a result
    set. An IDA occurs zero or more times within a desc, that is, it is a
    multiple-occurrence structure (the other component of a desc is a header,
    which is single-occurrence). Important fields in the IDA include: type,
    octet_length, length, data_pointer, octet_length_pointer. See also: DESCRIPTOR
    RECORD.

ITEM FIELD
    A field in an Item Descriptor Area.

ITEM QUALIFIER
    A Table or Correlation name, plus a period, preceding an asterisk in a select
    list.

ITEM REFERENCE
    A PSM term. A reference to a Column, SQL parameter or SQL variable.

ITERATE
    [1] We can repeat the code within a loop multiple times. Each time we go
    through is called one iteration of the loop

    [2] A PSM term. The "iterated SQL statements" are: LOOP, WHILE, REPEAT and FOR
    statements.

    [3] A PSM keyword. The statement format is: ITERATE <statement label>.

J
-

JAVA
    A computer language, used as an SQL host language but not in the SQL3 Standard
    definition.

JDBC
    The Java equivalent of ODBC.

JOB
    See: INSTANCE.

JOIN
    [1] A relational term. Combine two Tables and preserve the original Columns.
    (Thus a join in relational theory differs from a union, which ends up with the
    same number of Columns.) Generally joins are done with matching Column values
    (see equijoins).

    [2] A set-theory term. Any operation which combines two sets. (Thus unions and
    joins are the same thing in set theory.)

JOURNAL
    A file containing before/after copies, which can be used to recover if the
    main file becomes corrupt. We have preferred to use the word "log" to describe
    both this activity and the writing of files to record accesses or data
    changes. See: LOG.

JSQL
    A specification for embedded SQL within Java.

JULIAN
    [1] A calendar proposed by Julius Caesar, superseded by the Gregorian
    Calendar.

    [2] A date-numbering system proposed by Julius Scaliger, where each date is
    represented as a number = number of days elapsed since January 1, 4713 BC.

K
-

KB
    Short for kilobyte. 1024 bytes.

KEY
    [1] In standard SQL terminology: a set of Columns in a Tablel@@@@RAPHIC,
    ASCII_FULL, SQL_TEXT.

LEADING
    Appearing at tqe beginning of a string. Opposite of trailing. In the character
    strqng ' ABC' there is one leading space. Use "leading" instead of "leftmost"
    because (e.g.:) Arabs write from right to left. In a string of digits, tqe
    leading digit is the most significant digit. In the numeric string 01234 there
    is one leading zero.

LEAF
    (Of a Table) Having no proper subtables.

    (Of a type) Having no proper subtypes.

    The opposite is: maximal. See also: FINAL.

LEAVE
    A PSU term. The statement format is: LEAVE <statement label>.

LEFT JOIN
    An outer join, for which the Table which is specified is the inner Table. For
    example: if Table A has {'A','B','C'} and Table B has {'B',WC','D'} then A
    LEFT JOIN B produces: {'A' NULL, 'B' 'B', 'C' C'}.

LENGTH
    A measure which depends on units. For a BIT variable the length is in bits
    (see: BIT_LENGTH). For a CHAR variable the length is in characters or in bytes
    (see: OCTET_LENGTH). For most numbers, when we say "length" we really mean
    "precision" (see: PRECISION).

LETTER
    A character which is accepted as part of an alphabet (or, in exotic cases, as
    part of a syllabary). Thus the set of letters includes both Latin letters and
    accented letters, but not digits or special characters.

LEVEL
    [1] A level of conformance, such as Entry SQL or Intermediate SQL.

    [2] A level of isolation, such as READ UNCOMMITTED.

    [3] An occurrence in a series of Views.

LIKE
    An operator used for wildcarded character string comparisons. The predicate
    "'abcde' LIKE '%c%'" is TRUE.

LIST
    Not a formally defined word. In an SQL statement, a list is a series of items
    which all have the same type and are separated by commas: "select list",
    "parameter list", "Column list".

LITERAL
    A scalar value which is embedded within an SQL statement. Thus, in the
    statement "INSERT INTO Table_1 VALUES (5,'N')", we have a numeric literal (5)
    and a character literal ('N'). Literals are sometimes called "constants", but
    in the formal definin@@@@@@@@@@@ returns the lower-case equivalent of a character
    string. Thus LOWER('A. Smith') returns 'a. smith'. In SQL-92 the LOWER
    function only works for simple Latin letters. In SQL3 the LOWER function
    should work for any letter.

LOWER CASE
    A form of a letter in a Latin, Greek, Cyrillic, Georgian or Armenian alphabet.
    In English text, lower case is used inside words, not at the beginning of a
    sentence or proper name. The official (Unicode) name of a lower case letter
    always contains the word "small", e.g.: LATIN SMALL LETTER M.

M
-

MACHINE DATA SOURCE
    An ODBC term. The specification of a database and its associated DBMS which is
    accepted by an ODBC administrator program and stored in odbc.ini or in the MS-
    Windows95 registry.

MACRO
    An assembler term. An identifier which during the parsing process is
    translated to an expression. SQL example: (a) if "CREATE DOMAIN d CHAR(5);",
    then "CREATE TABLE Table_1 (Column1 d);" expands to "CREATE TABLE Table_1
    (Column1 CHAR(5));". The DBMS may treat a non-materialized View as a macro.

MANIPULATE
    (In a database) Access or change either the Schema or the data. Usually refers
    to data change statements.

MANTISSA
    [1] A mathematical term. The fractional part of a logarithm.

    [2] All approximate numbers have two parts: an exponent and a mantissa. For
    example, -1.234567E-02 has an exponent of -02 and a mantissa of -1.234567. In
    the IEEE floating-point standard, the mantissa size is a fixed number of bits.

MANUAL COMMIT
    An ODBC term. A mode, the opposite of AUTOMATIC COMMIT. In manual commit mode,
    the execution of statements has no permanent effect on the database -- nothing
    happens until you COMMIT and thus end the transaction. Manual commit mode is
    the default in SQL, but automatic commit mode is the default in ODBC. Note:
    the English meaning of the word "manual", i.e.: "by hand", is not implied.

MATCH
    [1] A SQL Standard term. Two keys match if all their components have the same
    values. A "partial match" can occur if some values are the same, others are
    NULL. See also: DUPLICATE.

    [2] A SQL Standard term. A character string matches a pattern if the <string>
    LIKE <pattern> returns TRUE or (in SQL3) if <string> SIMILAR TO pattern>
    returns TRUE.

MATCHLIST
    A list of the rows which match the criteria of a query. Usually the list
    consists of only the row's identifiers (as ROWIDs or as physical addresses)
    and so a matchlist is only visible internally in the DBMS. The external
    representation of a matchlist is a result set. See also: KEYSET.

MATERIALIZED VIEW
    A View whose rows take up space. When we select from a View, the DBMS can
    elect to do one of two things: (1) it can get the rows from the original
    Table, convert any derived Columns and pass the results to the application;
    (2) it can create a temporary Table and put the rows from the original
    Table(s) into that, then select from the temporary copy. The latter case is
    the materialized View case. Materialization is often necessary when there is
    no one-to-one correspondence between the original Table's rows and the View's
    rows (because there is a grouping) or when many Tables are affected and
    concurrency would be harmed (because there is a join).

MATRIX
    A mathematical term. An ordered array of values which are arranged in rows and
    Columns.

MAX
    An SQL keyword. MAX is one of the set functions. It is used to get the value
    in a Column which is greater than or equal to all other values.

MAXIMAL
    (Of a Table) Having no proper supertables.

    (Of a type) Having no proper supertypes.

    The maximal supertype is at the top of a UDT's type hierarchy and is sometimes
    called (mixed-metaphorically) the "root type". The opposite is: LEAF.

MB
    Abbreviation for megabyte. 1,048,576 bytes.

MEMBER
    Something which belongs to a set. Often, anything which meets the criteria for
    membership is automatically considered a member of a set.

MERGED COLUMN
    Also: derived Column. A Column in a Table which has been created with a set
    operator.

MESSAGE
    [1] A character string in the diagnostics area, with an
    implementation-dependent explanation of an exception or completion condition.

    [2] Information which is passed to or from a client or a server.

METADATA
    Data about data.

    [1] the data type, octet length, name, Collation etc. of a Column in a result
    set.

    [2] ditto for a parameter.

    [3] anything in INFORMATION_SCHEMA.

    [4] the data dictionary.

METHOD
    An object oriented term. In SQL3, a method is a function which is explicitly
    stated to be a component of a UDT (the other type of UDT component is an
    attribute). Some methods are defined automatically. See also OBSERVER
    FUNCTION, MUTATOR FUNCTION.

MIDDLEWARE
    An ODBC term. A piece of software that interposes between the application and
    the DBMS or between the components of a DBMS. For example, a routine that
    accepts English text as input, translates it to SQL, calls the DBMS, gets the
    results, converts them to English and outputs English text.

MIN
    An SQL keyword. MIN is one of the set functions. It is used to get the value
    in a Column which is less than or equal to all other values.

MINIMAL COMMON SUPERTYPE
    An Object/Relational term. For a set of UDTs {UDT1, UDT2}, the first type
    which is a supertype of both UDT1 and UDT2, traversing upward. Consider the
    family:

    ::

         Languages
              |
        --------------------
        |                  |
        Database           Conventional
        |                  |
        ------------       ----------
        |          |       |        |
        SQL        dBASE   Ada      Pascal

    The minimal common supertype for {SQL,dBASE} is Database. The minimal common
    supertype for {SQL,Ada} is Languages. For {Conventional,Pascal} the minimal
    common supertype is Conventional. If two types possess a common supertype,
    then by definition they are in the same "family".

MOD
    An SQL keyword. Short for modulus; however, in SQL MOD is used to get a
    remainder for two exact numeric arguments. Example: MOD(70,20) returns 10.

MODIFY
    Change either database or structure. Thus this term encompasses both "data
    change" and "Schema manipulation" and can refer to actions taken by either the
    application or the DBMS.

MODULE
    [1] An SQL Standard term. A group of SQL statements which are loaded together.

    [2] A file containing a program written in a host language.

MODULE LANGUAGE
    A specification for putting together SQL statements into programs which can be
    "executed" via the DBMS. Either there is no host language or the details of
    any host language translation are hidden from the programmer. The SQL Standard
    describes Modules at some length, but in the real world preference is given to
    one of the other binding styles: embedded SQL or CLI.

MODULO
    Ablative of "modulus". See: MOD.

MOST SPECIFIC TYPE
    [1] (Of a non-UDT value) The data type.

    [2] (Of a UDT value) The minimal subtype within a UDT hierarchy that can be
    used for the value. This will require a somewhat long example. ... Bonzo is a
    chimp. Chimps are primates. Primates are mammals. Mammals are animals.
    Therefore, Bonzo has four data types: chimp, primate, mammal or animal. But
    only one of those data types is the most specific type: CHIMP. ... However,
    suppose that we have a function with a primate parameter: CREATE FUNCTION ...
    (input PRIMATE) ... We can pass Bonzo to this function -- that's okay, he's a
    primate. But in that case, the "declared type" -- PRIMATE -- is not the same
    as the "most specific type" -- CHIMP. See also: DECLARED TYPE.

MONADIC
    Having only one operand and so distinguishable from niladic (having zero
    operands), dyadic (having two operands) and triadic (having three operands).
    Unary minus is a monadic operator. LOWER is a monadic function.

MULTI-VALUE KEY
    See: COMPOSITE KEY.

MULTIBYTE
    (Of a Character set) Having a variable number of octets in the encoding.
    Logically one should include as multibyte those fixed-width Character sets
    which require more than one byte, but it seems that doesn't happen in
    practice. See also: WIDE CHAR, VARIABLE-LENGTH ENCODING.

MULTICOLUMN
    (Of an index) See: COMPOSITE KEY.

MULTIMEDIA
    A set of extensions to the SQL Standard which ease the storage and access of
    sound, film, etc. Also known as SQL/MM.

MULTIPLE-TIER DRIVER
    A driver which is split into at least two parts (client and server) and
    usually into a third part as well (middleware).

MULTISET
    A set which may contain duplicates. In mathematics an ordinary set contains no
    duplicates, but SQL Tables often do, so perhaps we should have referred to
    things like result sets as result multisets. (The fact that SQL Tables are
    multisets rather than sets is also the reason that purists do not refer to SQL
    Tables as "relations".) The use of the word "bag" rather than "multiset" is
    rare.

MUMPS
    A host language which can be used with standard SQL (but frankly, SQL
    implementations which support MUMPS interfacing seem to be uncommon).

MUTATOR FUNCTION
    An Object/Relational term. A method for changing a single attribute in a UDT
    instance. Suppose you make a UDT thus: CREATE TYPE UDT1 (attribute1 BOOLEAN)
    ... The DBMS implicitly creates a mutator with this original method
    specification: "METHOD attribute1 (attr BOOLEAN) RETURNS UDT1 SELF AS RESULT
    LANGUAGE SQL DETERMINISTIC CONTAINS SQL RETURN NULL ON NULL INPUT". To change
    the value of attribute1, invoke the mutator method and pass the new value, for
    example: "u.attribute1(TRUE)" works (assuming u is an instance of UDT1). See
    also: OBSERVER FUNCTION.

MUTUALLY ASSIGNABLE
    An item of data type a and an item of data type b are mutually assignable if a
    can be assigned to b and b can be assigned to a. For example: we can assign
    the value 5 (which is an integer) to a FLOAT Column, because all numeric data
    types are mutually assignable.

MUTUALLY COMPARABLE
    An item of data type a and an item of data type b are mutually comparable if
    "a = b" is a legal expression. A counter-example: if x is a CHAR Column, then
    "... WHERE x = 5 ..." is a syntax error (because 5 is an INTEGER, rather thah@@@@@@@@@@TION STATEMENT
    The declarative statement in embedded SQL that begins with the words EXEC SQL
    WHENEVER.

EXCLUSIVE
    A type of lock. If Job #1 has an exclusive lock on row X, then Job #2 can
    neither read nor write row X. Compare: SHARED LOCK.

EXECUTE
    [1] Run. Do. Go. Execution is the activity of an SQL statement, or statement
    within a host language, which is distinct from preparation i.e.: from
    precompilation / preparation / binding.

    [2] A CLI term. Call the SQLExecute function.

EXISTS
    One of the SQL predicates, almost always associated with a correlated
    subquery, as in "SELECT * FROM T_1 WHERE EXISTS (SELECT * FROM T_2 WHERE
    T_2.col = T_1.col);" where the predicate means "such that there is a row of
    Table T_2 whose col Column equals a col Column in any row of T_1".

EXPLAIN
    Describe an access plan. This is a non-standard optional command in some
    DBMSs. For example, EXPLAIN might deliver the information that a query will be
    executed using an index.

EXPLICIT
    Right there in black and white. Specified. The reverse is implicit.

EXPLICITLY-ALLOCATED DESC
    An ODBC term. See: USER DESC.

EXPONENT
    A number within an approximate numeric literal, possibly signed, preceded by
    the letter E. The number indicates what power to raise 10 to. For example,
    15E+00 is "15 times 10 to the zeroth power (i.e.: 1)". See also: MANTISSA.

EXPONENTIAL NOTATION
    Also known as scientific notation or floating-point notation. In its standard
    form, exponential notation represents approximate numeric literals using: an
    optional sign, a decimal mantissa (usually between 1 and 10), the letter E, an
    optional sign and a decimal exponent. For example, the number 123 is
    represented in exponential notation as 1.230000E+02.

EXPORT
    To ship data out of the database. Usually this involves taking an entire
    Table's contents and converting it into a file format that can be read by
    non-DBMS programs.

EXPRESSION
    Any combination of operators and operands, yielding a value that can in turn
    be used as an operand. Sometimes expressions are classified by what they
    return ("value expressions" "Table expressions"), in non-standard texts
    expressions are classified by what they contain ("conditional expressions"
    "group expressions").

EXTENSION
    A feature which is not in the SQL Standard, generally requiring additional
    language. For example, indexes.

EXTERNAL ROUTINE
    [1] External here means "outside the (SQL) environment". A routine written in
    a host language which is called from SQL.

    [2] In any non-SQL context, an "external routine" is simply a routine in a
    different program.

EXTRACT
    An SQL integer function, which returns a component of a datetime. For example,
    EXTRACT (YEAR FROM DATE '1994-01-12') is equivalent to the integer 1994.

EXTREME FUNCTION
    Infrequent term. The aggregate functions MIN() and MAX() are collectively
    referred to as the "extreme" functions.

F

FALSE
    [1] In two-valued logic, a logical value which is not TRUE.

    [2] In SQL (which often uses three-valued logic), a logical value which is
    neither TRUE nor UNKNOWN. See also: LOGIC.

FAMILY
    An Object/Relational term.

    [1] Just as a human family may be thought of as the set of people who have (or
    are) a common ancestor, a "type family" is the set of all types with a common
    supertype. Since predefined data types or distinct types cannot have proper
    supertypes, the only type families which can have more than one member are
    structured types. For an illustration of a type family, see: MINIMAL COMMON
    SUPERTYPE. See also: HIERARCHY, STRUCTURED TYPE, MAXIMAL SUPERTYPE.

    [2] Similarly to [1], a "Table family" is the set of all Tables with a common
    supertable.

FEATURE
    A capability of a particular DBMS, to handle a certain data type or operation.
    With the CLI, one can find out about some DBMS features by calling the
    SQLGetInfo function. With SQL3, the features are in the SQL_FEATURES
    INFORMATION_SCHEMA View. For example, feature E091-5 is: can this DBMS do the
    SUM set function?

FETCH
    The act of taking a row, or a set of rows, out of a result set. The data and
    status indicators generally are transferred to buffers allocated by the host
    language program.

FETCH ORIENTATION
    One of: NEXT, FIRST, LAST, PRIOR, ABSOLUTE, RELATIVE. A modifier that tells
    the DBMS which direction to go in the result set, before fetching a row.
    Embedded SQL example: "EXEC SQL FETCH ABSOLUTE 55 Cursor_name INTO
    :host_variable :indicator_parameter;".

FETCH TARGET
    The host variable and indicator variable which will receive the value of a
    Column in a result, when FETCH happens. Fetch target addresses are specified
    in the ARD.

FIELD
    [1] An instance of a Column in a row of a Table. Thus, a scalar value which is
    taken from a row and Column intersection.

    [2] Loosely: a Column.

    [3] An SQL3 term. A (Field name, data type) pair within a row type. The Field
    value is the data type value.

FILE
    A persistent-storage object which often is physical (on disk), and often has a
    one-to-one relationship with an SQL persistent Base table. We reject the C
    standard definition: a sequence of bytes including disk files, pipelines and
    console input.

FILE-BASED DRIVER
    An ODBC term. A driver that contains a database engine instead of calling a
    database engine (as a "DBMS-based driver" does). Do not be misled by the word
    "file-based"; all ODBC drivers must ultimately perform file input/output at
    some level.

FILE SERVER
    An architecture, having to do with computers in a network. A file server does
    file operations (open/read/write/close etc.) but does not do higher-level
    database management operations (SELECT/UPDATE/etc.). Thus it differs from a
    client/server architecture. Because some people believe that file servers are
    relatively inefficient, they are becoming less common.

FINAL
    Part of a UDT definition. If a UDT is "final", it may not be a proper
    supertype -- that is, it may not be the object of an UNDER clause in a CREATE
    TYPE statement.

FIPS
    Abbreviation for [United States] Federal Information Processing Standard. The
    main document is FIPS PUB 127-2, Database Language SQL (30 pages), which
    helpfully specifies what the US government wants for some feature that the
    SQL-92 Standard says are "implementor-defined". The document is also issued as
    a package along with the SQL-92 Standard (ANSI X3.135-1992).

FIRE
    Execute (the SQL statements in a Trigger). The phrase "fire a Trigger" is
    popular but we do not use it in this book because the standard phrase is
    "activate a Trigger".

FIRST NORMAL FORM
    A relational term. A Table is in first normal form if there are no
    multiple-occurrence Columns. Since standard SQL-92 does not allow array
    definitions, this is fairly easy to achieve. See also: NORMALIZATION.

FIXED-LENGTH ENCODING
    An encoding for a Character set, in which all characters require the same
    amount of computer storage space -- generally one octet for the 8-bit sets for
    European languages, but two octets (16 bits) for the most popular
    manifestation of Unicode. See also: CODE PAGE, FORM-OF-USE, ISO 8859-X,
    VARIABLE-LENGTH ENCODING.

FIXED-LENGTH STRING TYPE
    CHAR and BIT Columns are "fixed-length" if they are not explicitly defined as
    VARYING. Insertions into such Columns are always padded on the right, so that
    every Column value has the same length. All character string literals and bit
    string literals are fixed-length.

FLAGGER
    A feature or utility provided by the DBMS vendor, which helps application
    programmers identify SQL language which is not standard, or which depends on
    implementation-specific language extensions. One way of doing this is to
    direct the precompiler to put marks in the embedded SQL source code program.

FLOAT
    One of the three approximate-numeric data types (the others are REAL and
    DOUBLE PRECISION).

FOLD
    A scalar function used on character strings to change case. The two fold
    functions in SQL are UPPER and LOWER. The two fold functions in ODBC are UCASE
    and LCASE.

FOR
    A PSM term. A keyword which introduces a "for statement", which takes the
    form: [<label> :] FOR <loop variable name> AS [Cursor details] <Cursor
    specification> DO <SQL statement list> END FOR [<ending label>]. See also:
    REPEAT, LOOP, WHILE.

FOREIGN KEY
    A set of Columns in a Base table, corresponding to some unique key. The
    foreign key is said to "reference" the unique key. Values in foreign key
    Columns must match values in referenced Columns. Usually the foreign key and
    unique key are in different Tables, and usually the unique key is a primary
    key.

FORM-OF-USE
    An encoding for a string of characters. In the western world most Forms-Of-Use
    are eight-bit or sixteen-bit fixed-length encodings. In Asia some Forms-Of-Use
    are variable-length encodings. An example of a Form-Of-Use is: the Windows
    code page. See also: ENCODING, CODE PAGE, ISO 8859-X, UNICODE, FIXED-LENGTH
    ENCODING, VARIABLE-LENGTH ENCODING, REPERTOIRE. Technical Note: Because a
    variable-length encoding may include escape characters which in effect cause
    the encoding method to change within a string, we define Form-Of-Use as an
    encoding for a string.

FORMAT RULE
    A rule about the structure and composition of tokens in an SQL statement. For
    example: "CREAT TABL Table_1 (x CHAR(5)" violates format rules. On the other
    hand: "CREATE TABLE Table_1 (x CHAR(0))" is cleanly formatted; however, it
    breaks a syntax rule. See also: SYNTAX RULE.

FORTRAN
    A language which can be used as a host language for SQL.

FORWARD-ONLY CURSOR
    A Cursor that can only go forward, i.e.: that supports "FETCH NEXT" operations
    but not "FETCH LAST", "FETCH ABSOLUTE", etc., as a scroll Cursor does.

FRACTIONAL PRECISION
    In a TIME or a TIMESTAMP or an INTERVAL which includes a SECOND field, the
    number of positions after the decimal point which indicate the fraction of a
    second. See also: SCALE, DECIMALDIGITS.

FREE
    [1] A CLI term. Tell the DBMS that a resource (env or dbc or stmt or desc) is
    no longer needed, usually via a call to SQLFreeHandle.

    [2] An SQL3 keyword. With FREE LOCATOR, for a BLOB, CLOB, NCLOB, ARRAY or UDT,
    we can cancel the association between a locator variable and its value.

FROM CLAUSE
    The word FROM followed by one or more Table references. For example this
    SELECT statement contains a FROM clause: "SELECT * FROM Table_1;". In the
    Standard, the term "FROM clause" is used only in the context of SELECT (not
    DELETE) statements.

FULL OUTER JOIN
    An outer join which fills in for non-matching values on both the left and the
    right. For example: if Table A has {1,3,5} and Table B has {1,2,3} then the
    full outer join of A and B has { 1 1, NULL 2, 3 3, 5 NULL}. See also: OUTER
    JOIN.

FULL SQL
    One of the levels of conformance of standard SQL-92, above Entry and
    Intermediate. An implementation which claims "full SQL conformance" is making
    a big claim.

FULL-TABLE SCAN
    If the DBMS must read every row in the Table and check whether the individual
    row matches a search condition, it's doing a full-Table scan. With big Tables
    this may be less efficient than alternatives such as indexed or hashed lookup.
    If the reading is from beginning to end (as it usually is) then a full-Table
    scan is synonymous with sequential search.

FUNCTION
    [1] A CLI term. A procedure, callable from a host language program, which
    returns a value. For example, all CLI functions return a 16-bit integer in
    return code.

    [2] An SQL-92 term. An operator which returns a single value, classified
    according to the number of operands (or parameters) following it: niladic
    function (no operands, e.g.: CURRENT_TIME), scalar function (one or more
    operands but from a single row, e.g.: UPPER), set function (one operand
    possibly from more than one row, e.g.: SUM). For the latter types, the word
    "function" may apply to both the operator keyword, and to the combination of
    the keyword and its (parenthesized) operands. See also: ROUTINE.

FUNCTIONAL DEPENDENCY
    A relational term.

    (Of a Column) Whose value can be derived (determined) via examination, by a
    human, of a value in another Column. Example #1: "If it's Tuesday this must be
    Belgium" (title of a movie about tourists, where one attribute -- location --
    is uniquely defined by another -- day-of-week). Example #2: "Since name =
    'Pinocchio', nose_size = 'large'". See also: NORMALIZE.

G
-

GATEWAY
    An ODBC term. A program which is called according to the CLI protocol for
    database X, and calls according to the protocol for database Y. Thus a gateway
    is middleware. An example is Micro Decisionware's "DB2 Gateway" which makes
    IBM's DB2 look accessible to SQL Server calls.

GENERAL CONSTRAINT
    Non-standard term. See: ASSERTION.

GENERAL RULE
    An SQL Standard term. A general rule specifies what is supposed to happen when
    an SQL statement executes. See also: ACCESS RULE, SYNTAX RULE.

GET DESCRIPTOR
    An embedded SQL term. A non-preparable statement which retrieves one or more
    fields from a descriptor area. Does the same job as the CLI's SQLGetDesc...
    functions. Example: "EXEC SQL GET DESCRIPTOR desc1 VALUE 1 :simple_target_spec
    = TYPE;".

GET DIAGNOSTIC
    An embedded SQL term. A non-preparable statement which retrieves one or more
    fields from a diagnostics area. Does the same job as the CLI's SQLGetDiag...
    functions. Example: "EXEC SQL GET DIAGNOSTICS :simple_target_spec =
    ROW_COUNT;".

GLOBAL
    Accessible from any Module: the scope is the SQL-session, rather than the
    Module. The term is most commonly encountered in embedded SQL and in the
    phrase "global temporary Table".

GLYPH
    A Unicode term. From the Greek "glupho": carve, write on a tablet. What a
    character looks like to a human after it is drawn or printed. As opposed to
    encoding -- what the bits are which are used to represent the character to a
    computer.

GMT
    See: GREENWICH MEAN TIME.

GRANT
    [1] An SQL verb. To give a Privilege (to a user).

    [2] Sometimes used as a synonym for the noun "Privilege"; the usage is
    somewhat inexact since not all Privileges can be explicitly granted.

GRANT OPTION
    A characteristic of a Privilege: can it be passed on to other users? If user a
    says "GRANT <Privilege> TO b WITH GRANT OPTION", then user b has the right to
    grant the Privilege to other users.

GRANTEE
    The object of a GRANT statement; the user who should receive the Privilege(s).
    Example: in the statement "GRANT SELECT ON Table_1 TO Sam;" Sam is the
    grantee.

GRANTOR
    The current user when a GRANT statement happens; the user who is granting the
    Privilege(s). Example: CONNECT ... (authorization-ID = Sally) then "GRANT
    SELECT ON Table_1 TO Sam;". Sally is the grantor.

GRANULARITY
    [1] (Of a lock) Bigness of locked area. From coarse to fine, the hierarchy
    usually is something like: "Table locking", "page locking", "row locking",
    "Column locking".

    [2] (Of a Trigger) Whether execution happens once per statement (FOR EACH
    STATEMENT), or happens once per row-change (FOR EACH ROW).

GRAPHIC
    (Of a character) Visible. Displayable. As opposed to a control character, but
    space is also a graphic character.

GRAPHIC_IRV
    See: ASCII_GRAPHIC.

GREENWICH MEAN TIME
    An obsolete standard for determining time displacement values, named after the
    Greenwich Observatory in England, longitude zero. See also: UTC.

GROUP
    A mathematical term. To combine elements of a set using a binary operator. For
    SQL the relevant operator is "duplicate", so an SQL group is formed by
    combining duplicate values.

GROUP BY CLAUSE
    A clause beginning with the words GROUP BY, used for lumping together
    duplicate values from detail rows, often for the purpose of summarizing.

GROUP FUNCTION
    Or Group-Value Function. See: SET FUNCTION.

GROUPED TABLE
    A set of rows produced by a GROUP BY clause or a HAVING clause. Each row is
    distinct, due to the definition of "group". Rows in grouped Tables may contain
    values from set functions.

GROUPED VIEW
    A View which contains an aggregate function, a GROUP BY clause or a HAVING
    clause in its definition.

GROUPING COLUMN
    A Column in a GROUP BY clause. The grouping Column is "what we group by". For
    example: if Table Table_1 has a Column c and "SELECT c FROM Table_1;" would
    produce {'A','B','A ','C',NULL,NULL} then "SELECT c,COUNT(c) FROM Table_1
    GROUP BY c;" would produce {'A' 2,'B' 1,'C' 1,NULL 2} and the grouping Column
    is c.

H
-

HANDLE
    A value, usually a 32-bit integer, which is used to refer to a resource. For
    example: ODBC has handles for environment, connection and statement. For
    example: DBMSs often store a BLOB's handle, rather than the BLOB itself, in
    the physical row of a Table file.

HANDLER
    [1] A routine which deals with exceptions. A handler is called when the SQL
    statement fails.

    [2] A PSM term. A handler is that which is declared by:

    ::

        <handler declaration> ::=
          DECLARE {CONTINUE|EXIT|UNDO} HANDLER
          FOR <condition value list>
          <handler action = SQL procedure statement>

    ... where a condition values is one of: a SQLSTATE value, a condition name,
    SQLEXCEPTION, SQLWARNING or NOT FOUND.

HASH
    A number (Often a 32-bit integer) which is derived from Column values (fields)
    employing a lossy compression algorithm. DBMSs occasionally use hashing to
    speed up access, but "indexes" are a more common mechanism.

HAVING CLAUSE
    A clause which begins with the word HAVING and contains a search condition.
    The HAVING clause is always associated with GROUP BY (although the GROUP BY
    may be implicit). The counterpart of a WHERE clause for grouped Tables.

HDBC
    A CLI term. The handle of a dbc (a connection resource). We use hdbc as an
    abbreviation for what the SQL Standard calls "handle of the SQL-connection".
    The sqlcli.h header file contains the line: ``typedef SQLINTEGER SQLHDBC /*
    connection handle */``. See: DBC.

HDESC
    A CLI term. The handle of a desc.

HENV
    A CLI term. The handle of an env. We use henv as an abbreviated substitute for
    the cumbersome SQL Standard term "handle of the allocated SQL-environment".
    The sqlcli.h header file contains the line: ``typedef SQLINTEGER SQLHENV /*
    environment handle */``. See: ENV.

HEXADECIMAL
    (Of a number) Using radix = 16 (or: number base 16). SQL numeric values are
    always decimal, but one can use hexadecimal numbers in bit or binary literals
    -- for example X'A74B'.

HEXIT
    One of: 0123456789ABCDEF. In the bit string literal X'0A', 0 and A are hexits.
    Although used by the standard, "hexit" is a rare word. Prefer "hexadecimal
    digit".

HIERARCHICAL DATABASE
    A database where all relationships between Tables are one-to-one or
    one-to-many, never many-to-many: "a servant cannot have two masters". For
    example: SALESREPS --> SALESREPS_SALES is one hierarchy and CLIENTS -->
    CLIENTS_SALES is another hierarchy, and it would be difficulty to "join"
    SALESREPS_SALES to CLIENTS_SALES. See also: RELATIONAL DATABASE.

HIERARCHY
    [1] The SQL Object hierarchy is: Cluster --> Catalog --> Schema --> Schema
    Object (Table, Domain, Constraint, etc.). See also: CLUSTER.

    [2] A "type hierarchy" or "UDT hierarchy" is a line of descent from supertypes
    to subtypes. For example, Animals to Mammals to Primates to Chimps -- Animals
    is the top of the hierarchy (the "maximal supertype"), Chimps is the bottom of
    the hierarchy (the "leaf type").

    [3] A "hierarchy option" is part of a Privilege descriptor, indicating that
    what is granted for a supertable is also granted for all subtables. See also:
    FAMILY.

HOLDABLE CURSOR
    A Cursor which remains open when the transaction is committed. This is
    abnormal; only in SQL3 may Cursors be declared as holdable.

HOST LANGUAGE
    A computer language used to write programs that interface with SQL. The
    standard host languages are: Ada, C, COBOL, Fortran, MUMPS, Pascal, PL/I.
    Other languages, such as Java and BASIC, are seen with some frequency in
    microcomputer circles. A program written in a host language is a "host
    language program". It will contain embedded SQL statements, or it will call
    SQL via a CLI.

HOST VARIABLE
    A variable defined in a host language program, which is passed (usually by
    address) to SQL. Usually the term "host variable" is used for embedded SQL
    only (for a CLI see: PARAMETER). The host variable is always preceded by a
    colon (:). An indicator may follow; the indicator is not considered part of
    the host variable. Embedded SQL snippet: "... EXEC SQL BEGIN DECLARE SECTION;
    x char[5]; EXEC SQL END DECLARE SECTION; ... EXEC SQL UPDATE Table_1 SET col =
    :x; ..." -- x is an input host variable.

HSTMT
    An unofficial abbreviation, used mostly within programs. In CLI applications
    we have a convention that h stands for handle and so hstmt is a handle of a
    stmt. So hstmt is what the SQL Standard calls "handle of the SQL statement".
    The sqlcli.h header file contains the line: ``typedef SQLINTEGER SQLHSTMT /*
    statement handle */``. See also: STMT, HDBC, HENV.

I
-

IBM
    A vendor. Makes "DB2" (short for: IBM Database 2) Universal Database, which in
    the past has had a great influence on the SQL Standard. www.ibm.com.

IDA
    See: ITEM DESCRIPTOR AREA.

IDEMPOTENT LAW
    A set theory term. "A UNION A" returns A, "A INTERSECT A" returns A.

IDENTIFIER
    An alphanumeric string by which one references an Object in SQL. Identifiers
    are subject to some restrictions -- must not be the same as a keyword, may
    contain only certain characters in certain places etc. -- so that the parser's
    job will be easier. An identifier is part of a name; no qualification is
    necessary if an identifier uniquely identifies an Object. An analogy: the name
    "Ralph Klein" refers to a person who may be referred to simply as "Ralph", but
    if there are two Ralphs in the room we would have to use the fully-qualified
    name "Ralph Klein". Here is an example of a qualified Table name which
    contains three identifiers: Catalog1.Schema1.Table1. See also: REGULAR
    IDENTIFIER, DELIMITED IDENTIFIER.

IDENTIFIER CHAIN
    A sequence of identifiers separated by periods. Usually the chain reflects
    part of the hierarchy of Objects: [Cluster.] [Catalog.] [Schema.] Schema
    Object. For Columns, the typical chain is [Table name.] Column name, or
    [Correlation name.] Column name. See also: QUALIFIER.

IDENTIFIER LENGTH
    The number of characters in an identifier. The SQL-89 standard says the
    maximum is 18. The SQL-92 and SQL3 standards say the maximum is 128. You can
    check by passing SQL_MAXIMUM_IDENTIFIER_LENGTH to the SQLGetInfo function. If
    you use non-Latin characters in identifiers, allow more than 128 octets in
    your application program buffers because characters might be 16-bit.

IDENTITY
    An operation which returns the same value as was in the input -- thus an
    identity operation on A is "A*1" or "A+0". In set theory, if you union S with
    the empty set you end up with S.

IEC
    Abbreviation for International Electrotechnical Commission.

IEF
    See: INTEGRITY ENHANCEMENT FEATURE.

IF STATEMENT
    A PSM term. An SQL conditional statement analogous to the "if" statements of C
    and Pascal. The usual format is "IF <search condition> THEN <statement list>
    END IF", or "IF <search condition> THEN <statement list> ELSE <statement list>
    END IF"; there is also provision for ELSEIF. If the search condition is TRUE,
    the THEN statement list is executed. If the search condition is FALSE or
    UNKNOWN, the ELSE statement list is executed (if any).

IMMEDIATE
    An SQL keyword. Without waiting. An EXECUTE IMMEDIATE statement both prepares
    and executes. A SET CONSTRAINTS ... IMMEDIATE statement activates all deferred
    Constraints.

IMPEDANCE MISMATCH
    A difficulty that arises when we bind SQL and host language programs, arising
    from the different rules (e.g.: SQL's use of three-valued logic) or slight
    incompatibilities in data types (e.g.: SQL's use of multiple Character sets).

IMPLEMENTATION
    [1] An SQL Standard term. A particular SQL DBMS, usually associated with a
    manufacturer and brand name and major version, in a context. For example "IBM
    DB2 as implemented on the OS/2 operating system". The Standard avoids using
    the words "DBMS", so one sometimes finds that for an official phrase -- such
    as "implementation row descriptor" -- one could substitute "DBMS row
    descriptor" and thus emphasize that we are talking about the DBMS's side of
    things, rather than the application's.

    [2] A client-server term. The implementation is both the client and the
    server, but not the application.

IMPLEMENTATION-DEFINED
    An SQL Standard term. A characteristic of an SQL DBMS left open by the
    Standard, which must be defined by the vendor, presumably in the manual. For
    example, the SQL-92 Standard says it is "implementation-defined" whether an
    SQL-Schema statement must form a separate transaction on its own. Distinguish:
    IMPLEMENTATION-DEPENDENT.

IMPLEMENTATION-DEPENDENT
    An SQL Standard term. A characteristic of an SQL DBMS left open by the
    Standard, which need not be, indeed perhaps should not be, defined by the
    vendor. For example, the SQL-92 Standard says it is "implementation-dependent"
    what the physical representation of data should look like, so you should
    regard the file format as ephemeral. Distinguish: IMPLEMENTATION-DEFINED.
    Because implementation-dependent is eight syllables, we sometimes avoid it and
    say "not specified" or "up to the vendor".

IMPLEMENTATION PARAMETER DESCRIPTOR
    Also IPD. A parameter descriptor whose information fields are set by the DBMS.
    As opposed to: APPLICATION PARAMETER DESCRIPTOR.

IMPLEMENTATION ROW DESCRIPTOR
    Also IRD. A resource, containing information about the Columns in a result
    set, as set up by the DBMS. It can be confused with the Application Row
    Descriptor which has corresponding fields; think of the distinction this way:
    the IRD describes the "bound Columns", while the ARD describes the "bound
    targets". See also: ARD.

IMPLEMENTOR
    The person or company who creates an implementation. See also: VENDOR.

IMPLICIT
    Unstated; tacit; taken as read. In the SQL statement "SELECT COUNT(*) FROM
    Table_1 HAVING COUNT(*) > 0;" there is an implicit GROUP BY. The reverse is
    EXPLICIT.

IMPORT
    To ship data into the database. Usually this involves the DBMS reading a file
    which has been produced by a non-DBMS program, and inserting in one of the
    database Tables.

IN
    An SQL keyword. An example of an IN predicate: "IN (a,b,c)" or "IN (SELECT
    Column1 FROM Table_1)".

INCLUDE
    A set-theory term. Set A is included in set B if all members of A are also
    members of B.

INDEX
    [1] A sorted set of keys and pointers, usually associated with one Column in a
    Base table, or with several Columns in the same Base table (in which case it
    may be called a "multi-Column index" or "concatenated index"). DBMSs often use
    indexes to speed up searches, but indexes are not mentioned in the official
    Standard. Alternatives are "full Table scans" and "hashes". Nowadays the usual
    plural seems to be "indexes" rather than "indices".

    [2] A CLI term. An integer which identifies an occurrence of an array For
    example, the RecordNumber parameter in the SQLGetDiagField function is
    sometimes called an index.

INDICATOR
    An integer variable defined in a host language program, whose value
    "indicates" whether the main ("data") variable is NULL, on both input and
    input. For example: the embedded SQL statement "EXEC SQL FETCH Cursor1 INTO :a
    :b;" puts a value into a (a is the data parameter) and a value in b (b is the
    indicator parameter); if the fetched value is 'x' then a gets 'x' and b gets
    0; if the fetched value is NULL then a is irrelevant and b gets -1
    (SQL_NULL_DATA). Also, in some situations, a positive indicator value is
    returned for a truncated string.

INFORMATION_SCHEMA
    The Schema that contains the Views that describe the database -- the metadata.
    For example, to find out what Domains exist, one would select from the DOMAINS
    View in INFORMATION_SCHEMA.

INFORMIX
    A vendor. Makes "Informix Universal Server". www.informix.com.

INGRES
    A vendor.

INHERIT
    Take the characteristics of what underlies. For example, a View Column
    "inherits" the data type of the underlying Base table Column. Inheritance goes
    from underlying to top, and so is the reverse of cascading.

INHERITANCE
    An Object/Relational term. A subtype inherits every component of a supertype.
    For example: if type t1 has two attributes -- t1_a and t1_b -- and we define a
    new type t2 UNDER t1, then t2 automatically has the attributes t1_a and t1_b;
    it may additionally have its own attributes (called its "non-inherited" or
    "originally-defined" attributes). SQL allows "single inheritance": although a
    type hierarchy can have indefinite length, and although a supertype may have
    many direct subtypes, a subtype may have only one direct supertype.

INITIALLY
    An SQL keyword, used in the definition of Constraints. An INITIALLY IMMEDIATE
    Constraint starts off as "a Constraint which must be checked when the SQL
    statement ends"; it may be INITIALLY DEFERRED (deferral is until COMMIT time
    or until SET CONSTRAINTS ... IMMEDIATE).

INLINE CONSTRAINT
    An Oracle term. A Constraint which is defined within parentheses.

INNER JOIN
    A type of Join which returns only values from existing rows. Inner joins are
    the normal garden variety join. See also: OUTER JOIN.

INNER TABLE
    For "a LEFT JOIN b" the inner Table is b. For "a RIGHT JOIN b" the inner Table
    is a.

INPRISE
    A vendor. Former name: Borland. Associated with Delphi and Interbase.

INPUT
    Directional adjective, thinking of the DBMS is the centre. Thus, an "input
    parameter" is a parameter for data going from the host language to the DBMS.

INSENSITIVE CURSOR
    If a Cursor is insensitive, then changes made outside the Cursor are not
    visible to the Cursor. By "changes made outside the Cursor" we mean any
    updates, other than UPDATE|DELETE ... WHERE CURRENT OF <Cursor>, which would
    affect rows currently in the Cursor or their definition. By "visible" we mean
    "seeable if we FETCH using the Cursor". If you open an insensitive Cursor,
    then FETCH with it and see X, then DELETE every row in the Table with some
    other Cursor, then FETCH with the insensitive Cursor again, you will still see
    X -- the DELETE happened but is not visible via the Cursor. See also:
    SENSITIVE, ASENSITIVE.

INSERT
    An SQL verb. We use INSERT to add a new row to a Table.

INSTALLER DLL
    An ODBC term. The ODBC administrator calls the installer DLL, which is often
    supplied by a driver vendor, in order to find out what the components are of a
    data source.

INSTANCE
    [1] A Windows term. Say you load WordPerfect twice in different windows.
    They're not the same program -- they're two copies of the same program, with
    different resource allocations, perhaps (but not necessarily) with different
    data. The two instances are "jobs", but we might reserve the word job for a
    running of WordPerfect on another computer.

    [2] An SQL Standard term. A "physical representation of a value" at a
    particular place in storage. For example, each row in a Table is one
    "instance" of a row type. An instance of a value occurs at a site.

INSTANTIABLE
    An Object/Relational term.

    (Of a structure-type UDT) Capable of being represented; not merely abstract;
    perhaps having instances. An instantiable UDT has a constructor function, may
    be used with "new" routines, and may be the UDT associated with a typed Table.

INTEGER
    [1] Exact numeric with scale zero.

    [2] An SQL predefined data type, signed, exact numeric, scale zero, precision
    implementation-defined. In most implementations precision is 31 bits and
    INTEGER values range from -2,147,483,647 (not -2,147,483,648) to
    +2,147,483,647. See also: SMALLINT, EXACT NUMERIC.

INTEGRITY
    [1] The maintenance of a consistent state despite transaction failure or
    crash.

    [2] Adherence to Constraints, especially Constraints which have to do with
    primary and foreign keys. The two general integrity rules are entity integrity
    (no primary key Column may be null) and referential integrity (no foreign key
    may reference a nonexistent key). The word "integrity" alone never means
    attribute integrity (the requirement that every Column value must be in the
    Column's Domain). See also: REFERENTIAL INTEGRITY.

INTEGRITY CONSTRAINT
    See: CONSTRAINT.

INTEGRITY ENHANCEMENT FEATURE
    Sometimes incorrectly called: integrity enhancement facility. An addition to
    the SQL-89 Standard, involving primary and foreign keys ("referential
    integrity"). Simpler integrity features, such as unique Constraints and NOT
    NULL modifiers, were already present in the SQL-86 Standard.

INTERACTIVE SQL
    See: DIRECT SQL.

INTERFACE
    [1] The routines, protocols and specifications which are needed to cross a
    boundary between subsystems, for example the CLI is the "Call Level
    Interface".

    [2] A descriptor area. The Standard refers to the APD, IPD, ARD and IRD as
    being four "types of interfaces".

    [3] An Object/Relational term. (Of a structured UDT) The set of all functions
    which include the UDT, either in the parameter declarations or as a return
    type. Example: suppose there are 50 functions (including methods). Of these,
    20 return type "UDT1", and ten others have an input parameter of type "UDT1".
    Those 30 functions together are the "interface of UDT1".

INTERMEDIATE SQL
    A level of SQL-92 conformance. An Intermediate SQL implementation can handle
    more of the SQL specification than Entry SQL, but less than Full SQL. All the
    well-known SQL-92 implementations today are Intermediate SQL.

INTERNATIONAL ORGANIZATION FOR STANDARDIZATION
    See: ISO.

INTERNATIONALIZATION
    Sometimes spelled i18n. The rules and processes which allow for different
    customs, languages or practices. SQL takes internationalization into account
    with its various Character set features; however, in standard SQL the datetime
    formats and decimal-point notations are always the same.

INTEROPERABILITY
    The likelihood that a host language program will run using two different
    DBMSs, without requiring changes to the SQL statements in it. In theory,
    interoperability should increase with adherence to standards. See also:
    PORTABLE.

INTERSECT
    Merge two Tables, accepting only rows which have values in common. See also:
    UNION, EXCEPT.

INTERVAL
    An SQL data type for representing the difference between two dates, between
    two times or between two timestamps.

INTERVAL LEADING FIELD PRECISION
    The components of an interval are called datetime "fields". The first field is
    the "leading field". The number of positions in this field is the "interval
    leading field precision". For example, in a year-to-month interval, year is
    the leading field and we would expect it to have 4 positions.

INTERVAL QUALIFIER
    One or three words, trailing an interval literal or part of an interval Column
    definition, indicating the start and end fields of the interval. One of: YEAR,
    MONTH, DAY, MINUTE, SECOND, YEAR TO MONTH, DAY TO HOUR, DAY TO MINUTE, DAY TO
    SECOND, HOUR TO MINUTE or HOUR TO SECOND. For example, in "INTERVAL '5-5' YEAR
    TO MONTH", the words "YEAR TO MONTH" are the interval qualifier.

INTRODUCER
    [1] In the Standard: an underscore preceding a Character set name.

    [2] By extension: the combination of the underscore and the Character set
    name. For example: _ASCII_FULL 'abcd' is a CHAR literal which contains an
    introducer -- that is, the literal is explicitly marked as being in the
    ASCII_FULL Character set. In SQL-92 introducers can precede either literals or
    identifiers; in SQL3 introducers may only precede literals.

    [3] The characters that signal a comment is starting, such as -- for simple
    comments or /* for bracketed comments.

INVALID
    (Of an SQL statement) Containing incorrect syntax.

    (Of a literal) Containing an illegal combination of characters.

    (Of a locator) Not referring to anything.

INVOCATION
    See: CALL STATEMENT.

IPD
    See: IMPLEMENTATION PARAMETER DESCRIPTOR.

IRD
    See: IMPLEMENTATION ROW DESCRIPTOR.

IS
    [1] An SQL operator used in predicates which test for NULL values: IS NULL or
    IS NOT NULL.

    [2] An SQL operator which permutes the result of a logical (such as a search
    condition): IS [NOT] TRUE, IS [NOT] FALSE, IS [NOT] UNKNOWN.

ISO
    Abbreviation for International Organization for Standardization. A large
    multi-function multi-country group which publishes standards. A branch of ISO
    is IEC, International Electrotechnical Commission, the group responsible for
    computer standards. Often ISO collaborates with ANSI so if there is an ANSI
    standard there is often an ISO standard which is nearly the same.

ISO 8859-X
    One of theerfluous. The DISTINCT operation removes all redundant
    duplicates, for example if there are two duplicate values 1 and 1 it removes
    the second duplicate, so that only one value remains.

REFERENCE
    [1] An SQL3 predefined data type. A reference value "points to" a row in a
    Base table which has the REF property.

    [2] See: REFERENCES.

REFERENCEABLE TABLE
    See: TYPED TABLE.

REFERENCED TABLE
    The Table that contains the primary or unique key which is the object of a
    foreign key REFERENCES clause. For example, for "CREATE TABLE Table_1 (...
    REFERENCES Table_2);", Table_1 is the referencing Table and Table_2 is the
    referenced Table. The Columns of the referenced Table's primary or unique key
    are the "referenced Columns".

REFERENCES
    (Of a foreign to a primary key Constraint) Is obliged to contain values which
    match.

REFERENCING TABLE
    The Table that contains a foreign key. For example, for "CREATE TABLE Table_1
    (... REFERENCES Table_2);", Table_1 is the referencing Table and Table_2 is
    the referenced Table. The Columns of the referencing Table's foreign key are
    the "referencing Columns".

REFERENTIAL ACTION
    What happens to a foreign key row if a corresponding row in a referenced Table
    is updated or deleted: CASCADE, SET NULL, DELETE or NO ACTION.

REFERENTIAL CYCLE
    A given Table may be both "referencing" (have a foreign key) and "referenced"
    (have a primary key), just as a son may also be a father. Any linked series of
    foreign keys which eventually leads back to the original Table is a
    referential cycle. See also: RECURSIVE.

REFERENTIAL INTEGRITY
    A database has referential integrity if all foreign key values are present in
    the corresponding referenced Tables. It is assumed in advance that the
    referenced Tables have primary keys and unique keys with unique values.

REGULAR IDENTIFIER
    Also "unquoted identifier". An identifier which is not enclosed in quotes.
    Used when assigning names to SQL Objects. In SQL-92, regular identifiers begin
    with {_ or letter}, contain only {_ or letter or digit} and have a maximum
    size of 128 characters. Unlike delimited identifiers, regular identifiers may
    not match reserved words and may not contain special characters. Case is not
    significant. See also: IDENTIFIER, DELIMITED IDENTIFIER.

RELATION
    A term from relational theory. A relation consists of a heading (the names of
    attributes) and a body (the attributes' values, multiple-occurrence). Since
    SQL is relational, some people use relational terms as synonyms for SQL terms:
    "Table" = "relation", "Column" = "attribute", "row" = "tuple". Doing so is
    dangerous if you don't keep in mind that there are slight distinctions: (a) a
    relation is a mathematical set while a Table is only a mathematical set if all
    rows are distinct; (b) a relation's attributes are considered unordered while
    a Table's Columns are ordered.

RELATIONAL DATABASE
    [1] Correct Definition: A database which should appear to consist solely of
    Tables. For the derivation of the word relational, see RELATION (previous
    entry).

    [2] Incorrect Definition: A database which contains Tables that are related to
    each other. Example (from an Oracle text): ** DRIVEL ** "The city name in one
    table is related to the city name in the other. This relationship is the basis
    for the name relational database."

RELATIONAL DATABASE MANAGEMENT SYSTEM
    Also RDBMS. A software package which supports all the relational operators and
    works only with relational databases.

RELATIONAL OPERATOR
    [1] A relational-theory term. One of: selection, projection, join. (There are
    others, but these are the terminals.)

    [2] (Not a recommended usage) A synonym for comparison operator.

RELATIONAL THEORY
    Not an SQL Standard term. We use it when referring to the writings of those
    who have proposed that set theory (including the concept of a "relation") can
    be applied in developing DBMSs.

RELATIVE
    An SQL Standard term. If we "FETCH ... RELATIVE +1" we get the next row --
    that is, going forward one compared to the current position. Compare:
    ABSOLUTE.

REMOTE DATABASE ACCESS
    Often abbreviated: RDA. A standard defining the low-level protocol for
    computers communicating SQL commands/results in a client/server environment.
    Standards: ANSI/IEC 9579-1 (generic model service and protocol), ANSI/IEC
    9579-2 (SQL specification). Mostly, these documents concentrate on the
    management of SQL databases via an OSI (Open Systems Interconnect) network.

REPEAT
    A PSM term. A keyword introducing a "repeat statement", which takes the form:
    [<label> :] REPEAT <SQL statement list> UNTIL <search condition> END REPEAT
    [<ending label>. See also: FOR, LOOP, WHILE.

REPEATABLE READ
    Suppose Sam reads row X from Table Y. Now Joe deletes that row. If Sam now
    reads again, will he see the same row as before? If the DBMS guarantees that
    he will, it supports repeatable reads. As an isolation level, REPEATABLE READ
    is below SERIALIZABLE but above READ COMMITTED. Note: the word "repeatable" is
    for concurrency contexts; for the case where the same DBMS can return
    different data regardless of concurrency, there is a different term: see
    DETERMINISTIC.

REPEATING SUBQUERY
    An obsolete term. See: CORRELATED SUBQUERY.

REPERTOIRE
    A Unicode term. Also: character repertoire. The distinct characters which are
    available in a Character set. Notice that we only say "characters" here, not
    "characters and their encodings". For example, the alphabet is a repertoire.
    See also: FORM-OF-USE.

REPLICATE
    Extract rows from a main database, which (after possible changes) can be
    merged back in much later. Replication is useful when there are mobile
    computers that are not permanently linked to the "server".

REPOSITORY
    [1] See: DATA DICTIONARY.

    [2] (external repository) A data collection which is directly managed by a
    non-SQL software package, which acts as a server to an SQL3 client, via UDT
    descriptions. Such, at least, is the dream of SQL/ERI (the SQL external
    repository interface), which may become a standard in a few years.

REPRESENTATION
    [1] To "represent" is to "stand for". If we say, as in ASCII, that the value
    65 stands for A, then the 65 is the representation of A in the ASCII encoding.

    [2] A general term. The way that a value is actually stored, for example (hex)
    0A is a representation of <newline>.

    [3] An Object/Relational term. The basis for a UDT definition. A distinct
    UDT's representation is a predefined data type; a structured-type UDT's
    representation is a list of attributes and methods.

REQUEST
    Any SQL statement or CLI function call -- seen as a "request" on the part of
    the application or user, that the DBMS please do something. The less polite
    word "Command" is usually used to denote a different concept.

REQUIREMENT
    A syntactical condition that must be satisfied for an SQL statement to work.
    For example, "DROP VIEW V CASCADE;" will fail (return a syntax error) if there
    is no View named V.

RESERVED WORD
    Also: Reserved Key Word. A word which cannot be used as an identifier because
    it is significant to the SQL parser. Not all keywords are reserved words.

RESET
    Obsolete term. When we unbind all parameters in an APD by setting the
    SQL_DATA_POINTER fields to zero, we use SQL_RESET_PARAMS. See also: UNBIND.

RESIGNAL
    A PSM term. An SQL keyword, starting a "resignal statement", which resignals
    an exception condition.

RESOURCE
    [1] A CLI term. There are four types of resources: env, dbc, stmt, desc.
    Resources are located by their handles: henv, hdbc, hstmt, hdesc. Resources
    and their handles are made by SQLAllocHandle functions and destroyed by
    SQLFreeHandle functions. Also called "CLI resource" or "allocated resource".

    [2] A general, non-standard term. Anything useable by a program, such as
    memory or disk space. Often seen in the phrases "lock a resource" or "allocate
    a resource".

RESTRICT
    [1] Also filter. A relational-theory term. Decide which rows will be operated
    on (using a predicate). The restrict operation picks the rows, the project
    operation picks the Columns.

    [2] An SQL keyword indicating that the DBMS should return an error if the
    conditions would require cascading; for example, if View V is based on Table
    T, then "DROP Table T RESTRICT;" should fail.

RESULT
    An ODBC term. Either a result set or a row count.

RESULT CODE
    See: RETURN CODE

RESULT SET
    A set of rows which is produced by a query (such as a SELECT statement). Since
    the correct application of a relational operation on a Table always results in
    another Table, a result set is a (derived) Table and the term "result Table"
    is occasionally used. But a result set is not a named Table which is
    permanently defined in the database. See also: MATCHLIST.

RESULT-GENERATING STATEMENT
    An ODBC term. An SQL statement that causes production of a result set. See:
    QUERY.

RETRIEVAL ASSIGNMENT
    An assignment to a target which cannot accept NULL or uses an indicator
    parameter to signify NULL. For example: a FETCH into a host variable.

RETRIEVE
    To take (a value) outside the DBMS's scope. Opposite of store.

RETURN CODE
    [1] A CLI term. The SMALLINT value returned by a CLI function, equivalent to
    SQL_SUCCESS, SQL_ERROR, SQL_INVALID_HANDLE, SQL_NO_DATA,
    SQL_SUCCESS_WITH_INFO, SQL_NEED_DATA, SQL_STILL_EXECUTING. Application program
    examples in this book frequently contain a line "SQLRETURN sqlreturn;" where
    SQLRETURN is a synonym for SMALLINT.

    [2] (Rare) The SMALLINT output parameter passed by reference to a CLI routine.

    [3] (Obsolete) SQLCODE. See also: NATIVE ERROR.

    [4] (Obsolete) SQLSTATE. See also: STATUS CODE.

RETURNED OCTET LENGTH
    The length in bytes of a CHAR or BIT or BINARY value which is returned in a
    descriptor area or to an indicator.

REVOKE
    An SQL verb. To take away Privileges (from users). See also: PRIVILEGES,
    GRANT.

RIGHT JOIN
    An outer join. In the expression "a RIGHT OUTER JOIN b" Table b is on the
    right. If there is a row in Table b which is not in Table a, the joined Table
    contains the Columns of the row in Table b and NULLs for each defined Column
    in a. For example: if Table a has {NULL,-1,0,1} and Table b has {0,1,2} then a
    RIGHT JOIN b produces {0 0, 1 1, NULL 2}. See also: OUTER JOIN, LEFT JOIN,
    FULL JOIN.

ROLE
    An SQL Standard term. A named Object, describing a collection of zero or more
    Privileges. Handy for granting and revoking bundles of Privileges at a time.
    Roles and users are in the same name space.

ROLL FORWARD
    Not an SQL Standard term. Update a database using information in a log. Often
    part of a recovery procedure.

ROLLBACK
    An SQL statement, the opposite of COMMIT. When we ROLLBACK, we cancel data or
    Schema changes that happened during the transaction and close all Cursors.
    Thus the database returns to its original state. Normally this original state
    is the state as of the last COMMIT, but SQL3 has an option for rollbacking to
    the last savepoint instead.

ROUNDING
    Adjusting to the nearest whole number after arithmetic operation, as opposed
    to truncation.

ROUTINE
    An SQL3 term. Either a function or a procedure. In a host language, the
    difference between a function and a procedure is that a function can return a
    value: the return code. The Standard's CLI document allows for implementations
    that contain return code in the parameter list (passed by reference so it can
    receive values). But in practice, if the host language is C or Pascal, expect
    functions.

ROUTINE NAME
    An SQL3 term. One of the ways that a routine can be identified, (the other is
    SPECIFIC NAME). The routine name is what you "call" when you use procedures or
    functions, including methods. However, a routine name may not be unique within
    a Schema, so the DBMS may need further information when it chooses which
    routine to execute. See also: SIGNATURE, PATH.

ROW
    [1] An SQL Standard term. A sequence of (Field name, value) pairs -- that is,
    the header and the instance are both theoretically part of the "row". But in
    practice we usually forget about the Field name.

    [2] A sequence of Columns. (Remember that "sequence" implies "ordered".) In
    relational terms, a "tuple". Often used as a synonym for record. In this sense
    a row is a container where we place a sequence of values.

    [3] The horizontal component of a Table (the vertical component is a Column).

ROW CONSTRUCTOR
    See: ROW VALUE CONSTRUCTOR.

ROW DESCRIPTOR
    A CLI term. The description of a result set's Columns. There are two kinds:
    implementation row descriptors (IRDs) and application row descriptors (ARDs).

ROW IDENTIFIER
    See: ROWID.

ROW NUMBER
    The number of a row within a result set, beginning with 1. See also: ROWID.

ROW STATUS ARRAY
    An ODBC term. An array of values for multiple-FETCH operations used by
    ODBC-specific CLI functions SQLExtendedFETCH or SQLFETCHScroll, reflecting
    success/failure for each individual row fetched.

ROW SUBQUERY
    A subquery which returns a single row. For example: "SELECT * FROM Table_1
    WHERE (c1,c2) = (SELECT c1,c2 FROM Table_2);". The row subquery is not common.
    The other kinds of subqueries are: scalar subquery, table subquery.

ROW TYPE
    An SQL3 term. A data type which is constructed with the word ROW (the other
    constructed types are REF and ARRAY). A row type is described as a sequence of
    Fields.

ROW VALUE CONSTRUCTOR
    Also row constructor. A parenthesized expression containing a comma-delimited
    series of columnar values -- for example "(a,5,b)". Seen in OVERLAPS
    predicates, VALUES statements and (uncommonly) in other predicates.

ROWID
    An Oracle term. A Column which contains a row's address. Useful for direct
    access to a row, but frowned on by relational purists. See also:
    SELF-REFERENCING COLUMN.

ROWSET
    An ODBC term. Sometimes two words: row set. In ODBC it is possible to retrieve
    two or more rows from a result set. For example you can FETCH "a set of n
    rows" into an array. Also: the set of rows returned by a block-Cursor
    operation. In standard SQL you can only FETCH one row at a time, so in
    standard SQL there is no need for the term "rowset". Try not to confuse this
    with: result set.

ROWSET BUFFER
    An ODBC term. Data area allocated by host program, used by SQLExtendedFETCH or
    by SQLFETCHScroll, containing data and statuses for multiple fetched rows.

RULE
    [1] (Obsolete) Constraint.

    [2] A statement in the SQL Standard which is preceded by the words General
    Rule, Syntax Rule or Access Rule. See also: REQUIREMENT.

RUNTIME
    A non-standard term. Runtime is a period (not an interval) during which an SQL
    statement is being executed.

S
-

SAG
    Abbreviation for SQL Access Group. A consortium for SQL Standards.
    Generalizing: SAG membership is more commercial than ANSI's or ISO's and SAG's
    orientation is more toward the CLI than the SQL grammar. Historically, SAG's
    original mandate was for connections (e.g.: RDA). We respect SAG but usually
    when we say "standard SQL" we mean "ISO standard SQL". However, there is
    rarely significant conflict. Often SAG gives a specific prescription where ISO
    says "implementation-defined"; compare the action of other non-ISO standard
    bodies like FIPS and X/Open.

SATISFY
    An SQL Standard term.

    [1] An SQL statement "satisfies the conditions" of a syntax or access rule if
    it avoids violating it.

    [2] (Of a CHECK clause in a Constraint) Not FALSE -- that is, a CHECK clause
    is satisfied if it is either TRUE or UNKNOWN.

    [3] (Of a HAVING clause) TRUE -- that is, a HAVING clause is satisfied for a
    given grouped row if it is TRUE, period.

SAVEPOINT
    An SQL3 term. A named moment during a transaction which can
    be the object of a ROLLBACK statement. That is, with SQL3 a ROLLBACK may
    specify that only those statements which are "subsequent to savepoint <s>" are
    to be cancelled, or rolled back. SQL statements exist for creating and
    releasing savepoints.

SCALAR FUNCTION
    A function which returns a single value given a single-value argument.
    Example: "OCTET_LENGTH (column_5)". However, AVG is not a scalar function but
    a set function (it returns a scalar value but its input is not scalar).

SCALAR OPERATOR
    An operator which takes scalar values as operands and returns a scalar value.
    For example: "+" is a scalar arithmetic operator and ">" is a scalar
    comparison operator.

SCALAR SUBQUERY
    A subquery which returns a scalar value. Example: SELECT (SELECT MAX(n) FROM
    Table_1) FROM Table_1);. The other kinds of subquery are: row subquery, Table
    subquery.

SCALAR VALUE
    A single value. The types of scalar values are: parameter / host language
    variable, Column instance, literal, or expression containing any of the
    previous. A compound item, such as a row, has more than one scalar value.

SCALE
    The number of positions after the radix point. Since we deal in decimal
    numbers, we can define scale as the number of digits after the decimal point.
    Scale applies only for exact numeric data types: INTEGER and SMALLINT (which
    have a scale of 0) or DECIMAL and NUMERIC (which have a user-specified scale).
    See also: FRACTIONAL PRECISION.

SCHEMA
    The level of the SQL Object hierarchy below a Catalog. A named group of
    Tables/Domains/Constraints/Character sets/etc. which is owned by a single
    user.

SCHEMA DEFINITION STATEMENT
    An SQL Standard term. One of: CREATE, GRANT. See also: SCHEMA MANIPULATION
    STATEMENT, SCHEMA STATEMENT.

SCHEMA MANIPULATION LANGUAGE
    Abbreviation: SML. Obsolete. See: SCHEMA MANIPULATION STATEMENT.

SCHEMA MANIPULATION STATEMENT
    An SQL Standard term. One of: ALTER, DROP, REVOKE. See also: SCHEMA DEFINITION
    STATEMENT, SCHEMA STATEMENT.

SCHEMA STATEMENT
    An SQL Standard term. One of: CREATE, DROP, ALTER, GRANT, REVOKE. See also:
    SCHEMA DEFINITION STATEMENT, SCHEMA MANIPULATION STATEMENT.

SCIENTIFIC NOTATION
    See: EXPONENTIAL NOTATION.

SCOPE
    The horizon beyond which an identifier is not visible. For example, in C a
    variable's scope may be the process or the module or the program. For example,
    in the SQL statement "SELECT C1 FROM Table_1 WHERE C1 = (SELECT C2 FROM
    Table_2 WHERE C2 = 5)", the scope of the inner SELECT is bounded by the
    parentheses. Most SQL Objects, except temporary Tables, have global scope
    i.e.: they can be seen by any SQL statement and in any Module.

SCROLL CURSOR
    A Cursor whose result set you can go both forward or backward in. (With a
    regular or non-scroll or forward-only Cursor you can only "FETCH NEXT".)

SEARCH CONDITION
    A predicate or combination of predicates. Thus, "a = b OR b = c" is a search
    condition (which happens to contain two predicates that are merged by a
    Boolean operator). A search condition can occur within a WHERE clause, a
    HAVING clause, an ON clause, a CHECK clause or a CASE expression. A search
    condition returns a value of data type BOOLEAN: TRUE or FALSE or UNKNOWN. For
    example: assume a Table T that has a Column c and a single row, containing
    NULL. If we execute the query "SELECT * FROM T WHERE c = 5;" -- the result of
    the search condition "c = 5" is UNKNOWN for the single row, the WHERE clause
    rejects all FALSE or UNKNOWN results, so the result of the query is an empty
    result set.

SEARCHED OPERATION
    An UPDATE statement (searched UPDATE) or DELETE statement (searched DELETE)
    which is not a positioned operation, that is, contains no WHERE CURRENT OF
    clause. Examples: "UPDATE Table_1 WHERE c=5;", "DELETE FROM Table_1;".

SECOND NORMAL FORM
    A relational term. There are no Columns which functionally depend on only one
    Column of a multi-Column primary key. For example, the following Table is not
    in second normal form: "CREATE TABLE Monthly_Expenses (employee_name CHAR(10),
    expense_month INT, employee_sex CHAR(100), amount DECIMAL(5,2), PRIMARY KEY
    (employee_id, expense_month));" -- presumably employee_sex functionally
    depends on employee_name alone. See also: FIRST NORMAL FORM, FUNCTIONAL
    DEPENDENCE, NORMALIZATION, PRIMARY KEY.

SECURITY
    Rules and operations which prevent or inhibit access of data by unauthorized
    users. The basic SQL security model consists of authorizations, users, Roles,
    Privileges, GRANT and REVOKE statements, the concept of Schema ownership and
    access rules. See also: INTEGRITY.

SELECT CLAUSE
    Bad usage. Everything preceding the word FROM in a SELECT query expression.
    See: SELECT LIST.

SELECT EXPRESSION
    A term used by C.J.Date. A synonym for the standard term: query specification.

SELECT LIST
    A list of Columns/expressions, between the word SELECT and the word FROM, in a
    SELECT statement. The components of a select list, which are separated by
    commas, can be either "[qualifier.]*" or derived Columns which are specified
    as: "value expression [AS derived Column name].

SELF JOIN
    A join of an instance of a Table to another instance of the same Table. For
    example, if Table a has three rows {1,2,3}, then "SELECT ... FROM a,a;" will
    produce nine rows: {1 1, 1 2, 1 3, 2 1, 2 2, 2 3, 3 1, 3 2, 3 3}.

SELF-REFERENCING COLUMN
    An Object/Relational term. A unique Column in a typed Table, whose data type
    is REF(type) For example: for "UDT1" is a UDT name, "CREATE TABLE Table_1 OF
    "UDT1" REF IS c SYSTEM GENERATED" -- Table_1 is a typed Table and c is the
    Table's self-referencing Column. Since a row in this Table can be thought of
    as an instance of the Table's UDT and since a UDT is analogous to a "class",
    the self-referencing Column is analogous to what object-oriented folk call an
    "object identifier" (OID). The value of a self-referencing Column is decided
    at INSERT time; the Column cannot be updated. The types of self-referencing
    Column are: system generated, user generated and derived.

SEMIRELATIONAL
    (Of a DBMS) Following rules for a relational system, but not exclusively. For
    example, a DBMS which allows searches via pointer navigation as well as by
    relational joining.

SEPARATOR
    A character in an SQL statement which helps the parser realize that one token
    has ended and another is beginning. The clearest separators are spaces. Other
    separators are: newline (carriage return and/or line feed) and comments. See
    also: DELIMITER TOKEN.

SEQUEL
    Originally, SEQUEL was the API for an early (circa 1974) IBM relational
    database system, System R. Later the names SEQUEL and SEQUEL/2 were applied to
    the language and later still the name was changed to SQL. The name SEQUEL
    stood for "Structured English Query Language" and "SQL" is often pronounced
    "sequel" to this day.

SEQUENCE
    [1] A set-theory term. A set which is written in a particular order. Thus
    {1,7,8} and {8,1,7} are two different sequences of equal sets. In SQL3,
    sequences may be multisets.

    [2] A CLI term. The order of execution. You get a "function sequence error" if
    you call functions in the wrong order.

SEQUENTIAL
    [1] A search strategy: read the first row in a file and check whether it
    matches the query, then read the second row, then the third, etc. (without
    indexes or other speed-up tricks). See also: FULL-TABLE SCAN.

    [2] The opposite of concurrent.

SERIALIZABLE
    Two transactions are serializable if the effect of running them concurrently
    is the same as running them sequentially.

SERIES
    [1] A set theory term. A series is a sequence in which the components are
    separated by some operator, usually +, as in "1+2+3+4".

    [2] Loosely: a synonym for sequence. For example: "serializable" must mean
    "capable of being put in a sequence".

SERVER
    A central program in a client/server environment. The server is responsible
    for accessing a database and returning information to a client.

SESSION
    Also SQL-session. The sequence of database related activities which takes
    place for an instance of a Module, in the period of time between the execution
    of CONNECT and DISCONNECT statements. In CLI contexts, the word "connection"
    is used instead of "session".

SESSION STATEMENT
    Also SQL-session Statement. One of: SET LOCAL TIME ZONE, SET SESSION
    AUTHORIZATION. In SQL3, add: SET ROLE, SET SESSION CHARACTERISTICS.

SESSION_USER
    An SQL niladic character string function, which returns the identifier of the
    user associated with the current SQL-session. See also: CURRENT_USER,
    SYSTEM_USER.

SET
    [1] A mathematical term. An enclosure of values that have something in common.
    SQL is sometimes said to be a "set-oriented language", but see also: MULTISET,
    RELATION.

    [2] An SQL verb, used when changing various options and flags: SET CONNECTION,
    SET CONSTRAINTS, SET DEFAULT, etc.

    [3] An SQL keyword, meaning "assign", in the UPDATE statement.

SET CONDITION
    Obsolete. An operator that returns a set of records.

SET FUNCTION
    One of the five built-in SQL functions:  AVG, COUNT, MAX, MIN, SUM, GROUPING,
    EVERY, ANY, SOME. A set function differs from a scalar function because the
    input is a collection; however, the output is a scalar value. Often set
    functions are found in the context of GROUP BY and HAVING clauses, but not
    necessarily. The popular but non-standard term for set function is "aggregate
    function".

SET OPERATOR
    One of the three operators that merge sets: UNION, EXCEPT, INTERSECT.

SET QUANTIFIER
    See: QUANTIFIER.

SET STATEMENT
    A PSM term. The statement which assigns values to items. The format is: SET
    <target> = <source>. The target can be a variable or parameter (not a Column
    reference). The source can be a value expression.

SET THEORY
    A branch of mathematics. Pioneered by Georg Cantor. Used as a theoretical
    basis for SQL.

SHAPE
    The box outline of a picture of a Table. Formally: an occasional term for
    describing a Table's degree, Column names, data types and other descriptive
    details.

SIGNAL
    A PSM term. An SQL keyword, starting a "signal statement", which signals an
    exception condition.

SIGNATURE
    An SQL3 term. Information used to identify the correct SQL routine to call.
    The routine name alone may be insufficient, since two routines in the same
    Schema may have the same name. However, the statement "CALL R (x)" contains
    enough information, namely: it's implied that R is a procedure, the routine
    name is R and there is one parameter with the declared type of x. A complete
    signature includes: routine type (procedure or non-method function or static
    function or overriding function), routine name, parameter count and parameter
    types. See also: PROTOTYPE.

SIGNED NUMBER
    A number which may be preceded by + (positive) or - (negative). In SQL all
    predefined numeric data types are for signed numbers.

SIGNIFICANT
    The digits in a number, between the last leading zero and the first trailing
    zero. All the following numbers have 3 significant digits: 3.14, 003.1400,
    999.

SIMILAR
    An SQL3 keyword. The SIMILAR predicate works much like grep (the general
    regular expression parser) in Unix. Its syntax and usage are pretty well the
    same as for the LIKE predicate, but SIMILAR has more pattern options.

SIMPLE COMMENT
    A comment which begins with -- and continues to the end of the line.

SIMPLE KEY
    A key based on a single Column. Opposite of composite key.

SIMPLE LATIN LETTER
    A Latin letter which is not an accented letter.

SIMPLE TABLE
    One of: a query expression, a Table value or an explicit Table.

SIMPLE TARGET SPECIFICATION
    A target specification with no indicator. See also: TARGET SPECIFICATION.

SIMPLE VALUE SPECIFICATION
    A parameter or a host variable, with no indicator. See also: VALUE
    SPECIFICATION.

SINGLE QUOTE
    See: QUOTE.

SINGLETON SELECT
    An embedded SQL term. A SELECT which can return at most one row. For example:
    "EXEC SQL SELECT <Column> INTO :host-variable ...;". In effect, this combines
    into one statement the DECLARE, SELECT, OPEN, FETCH and CLOSE operations. But
    it's an error if the SELECT returns more than one row.

SITE
    A place which is occupied by an instance of a value. Thus a site can be
    thought of as a physical storage unit, such as a page of RAM or a file
    location. Sites may be transient (e.g.: the address of a return code),
    temporary (e.g.: a resource) or persistent (e.g.: a Schema description). A
    Base table can be either a temporary or persistent site.

SKELETON
    A CLI term. If an SQLAllocHandle call fails, the DBMS is sometimes able to
    return a handle anyway -- but this handle is not fully functional, all you can
    do with it is get diagnostics. Such a handle is a "skeleton".

SMALL LETTER
    See: LOWER CASE LETTER.

SMALLINT
    One of the exact numeric data types with fixed scale of zero (the other
    standard one is INTEGER). In practice, always a signed 16-bit value with a
    range between -32767 (not -32768) and +32767.

SOME
    An SQL key word. A synonym for ANY. See: ANY.

SORT
    To arrange values in a sequence which is defined by the characteristics of the
    data type (for example an ascending number sequence has +5 following -5) and
    by the Collation. In SQL, the ORDER BY clause ensures sorted results.

SOURCE
    Where something is coming from, as in the "source Character set" (the
    Character set which is used as a basis for CREATE CHARACTER SET), the "source
    value" (the value which we "assign" to a "target"), the "insert source" (the
    rows in an INSERT statement's query expression) and so on.

SOURCE CODE
    A character string containing statements. If the statements are SQL
    statements, the DBMS may prepare and execute them.

SPACE
    A character which is present in all SQL Character sets. The ASCII encoding for
    space is 32. Among other things, spaces are separators and pad characters. See
    also: WHITE SPACE.

SPARC
    Abbreviation for Standards Planning And Requirements Committee.

SPECIAL CHARACTER
    A character which does not appear in an alphabet and is not a digit. The SQL
    special characters are: / : ; " % & ' ( ) * + , - . < = > ? _ | and space.

SPECIAL VALUE
    An obsolete term. See: NILADIC FUNCTION.

SPECIFIC
    [1] The phrase "most specific type" refers to the type which cannot be broken
    down into subtypes, i.e.: an atomic type for which all others are supertypes.
    By extension: the "specific" type TIMESTAMP WITHOUT TIME ZONE is classed with
    the generality: datetime.

    [2] In general, the SQL Standard uses the word "specific" for a single
    particular instance of some group, but it is not a synonym for "specified".

SPECIFIC NAME
    An SQL3 term. A routine can have two names: the routine name and the specific
    name. The specific name, which may be automatically created by the DBMS in an
    implementation-dependent fashion, may be qualified. Unlike routine names,
    specific names are unique (but there is another way to uniquely identify a
    routine: see SIGNATURE). Sometimes one uses specific names for actions other
    than "call", for example: "DROP SPECIFIC ROUTINE <specific name> CASCADE;".
    See also: ROUTINE NAME.

SPECIFICATION
    A word used within terms that imply singularity. Thus, a value specification
    is a value which contains one operand and no operators; a query specification
    is a simple query which contains no UNIONs or the like.

SQL
    [1] An SQL Standard term. The language described by the ISO Standard SQL
    documents.

    [2] A popular term. Pronounced "Sequel". Stands (unofficially) for Structured
    Query Language. A (sub)language for accessing computer databases. See also:
    SEQUEL.

SQL CONFORMANCE LEVEL
    Reflects the fullness with which a particular SQL implementation supports an
    SQL Standard.

SQL DATA TYPE
    See: DATA TYPE.

SQL DATA TYPE CODE
    See: DATA TYPE CODE.

SQL LANGUAGE CHARACTER SET
    See: SQL_CHARACTER.

SQL PROCEDURE STATEMENT
    See: PROCEDURE STATEMENT.

SQL ROUTINE
    A PSM term. A routine which is written in SQL and invoked from SQL.

SQL SERVER
    See: MICROSOFT or SYBASE.

SQL STATEMENT
    See: STATEMENT.

SQL STATEMENT IDENTIFIER
    See: STATEMENT IDENTIFIER.

SQL-TRANSACTION STATEMENT
    See: TRANSACTION STATEMENT.

SQL-
    Some words that begin with SQL- can be found under their unprefixed
    equivalents. Example: for "SQL-Schema" see "Schema".

SQL-89
    See: ISO STANDARD SQL.

SQL-92
    Formerly known as SQL2. The official standard before SQL3 and what will be the
    de facto "official" standard for some years to come. ANSI X3.135-1992 (as
    amended by Technical Corrigendum 3), ANSI/ISO/IEC 9075-3(1995) for the CLI,
    ANSI/ISO/IEC 9075-4(1996) for persistent Modules and ANSI/IEC 9759-2 for
    remote data access. See also: ISO STANDARD SQL.

SQL-CONNECTION STATEMENT
    See: CONNECTION STATEMENT.

SQL-CONTROL STATEMENT
    See: CONTROL STATEMENT.

SQL-DATA
    See: DATA.

SQL-DATA STATEMENT
    See: DATA STATEMENT.

SQL-PATH
    See: PATH.

SQL-SCHEMA STATEMENT
    See: SCHEMA STATEMENT.

SQL-SERVER MODULE
    A PSM term. A Module that is a Schema Object.

SQL-SESSION STATEMENT
    See: SESSION STATEMENT.

SQL TRANSACTION
    See: TRANSACTION.

SQL2
    The original designation for what is now SQL-92.

SQL3
    The original designation for the latest version of the SQL Standard. The name
    will probably change, just as "SQL2" became "SQL-92".

SQL4
    Some stuff that will still be undone when SQL3 comes out. For example:
    enumerated data types and null classes.

SQLCA
    A host language data structure containing basic information for SQL
    applications, such as error returns and sometimes row counts.

SQLCLI.H
    A header file used in CLI applications. C programs may begin with "#include
    sqlcli.h". Prototypes and definitions in sqlcli.h are suggested in an appendix
    of the Standard; it is not required that an SQL-conforming program use
    sqlcli.h.

SQLCODE
    In SQL-92 and earlier, an integer representing a completion state of an SQL
    statement. For example: 0 is okay. For example: -966 is not okay. No longer
    supported for SQL3 -- see: SQLSTATE.

SQLDA
    A host language data structure containing information for dynamic SQL
    applications. Although some DBMSs still support the SQLDA, the modern style is
    to let the DBMS store the structure. See: ARD, IRD.

SQLJ
    Abbreviation for "SQL - Java". The embedded SQL variant for Java. See also:
    JDBC.

SQLSTATE
    A five-character output parameter containing a status code for an SQL
    statement: okay, warning, error. For example: '00000' is okay. For example:
    '22008' is an error.

SQL_CHARACTER
    Also: SQL language Character set. The set of 83 characters which are
    meaningful in SQL key words or symbols. In SQL3 and the FIPS specification: a
    predefined Character set. Other predefined Character sets are: ASCII_GRAPHIC,
    LATIN1, ASCII_FULL, SQL_TEXT, UNICODE.

SQL_TEXT
    A predefined Character set. SQL_TEXT is a superset of all other Character
    sets, that is, any character in another set is also in SQL_TEXT. The SQL_TEXT
    set is used for SQL identifiers. Other predefined Character sets are:
    ASCII_GRAPHIC, LATIN1, ASCII_FULL, SQL_CHARACTER, UNICODE.

STANDARD
    [1] (As used in this book) ISO Standard SQL or proposed modifications thereof.

    [2] (Another common and acceptable usage) SQL syntax recognized by more than
    one vendor, also known as "de facto standard".

    [3] See: ISO STANDARD SQL.

STATE
    [1] (Of a Cursor) Open or closed.

    [2] (Of a database) The values of all data and metadata items at a given
    moment. Any data change or Schema change statement causes a change in state.

    [3] An SQL3 keyword for a function associated with UDTs.

    [4] An object oriented term. The ordered sequence of an object's instance's
    attributes, excluding the object identifier -- see: ROW.

STATEMENT
    [1] Also "SQL Statement". A string containing SQL keywords, structured
    according to the rules of SQL syntax, designed for passing instructions to the
    DBMS.

    [3] Also "Allocated SQL statement". A standard CLI term. See: STMT.

    [4] A set theory term, not to be used. See instead: SEARCH CONDITION.

STATEMENT HANDLE
    See: HSTMT.

STATEMENT IDENTIFIER
    Also: command function. A short (one-word or two-word or three-word) string
    based on the general classification of an SQL statement. Usually SQL statement
    identifiers are based on the most important keywords in the statement and are
    used for diagnostics messages. The Standard SQL3 statement identifiers are:
    ALTER DOMAIN, ALTER TABLE, CALL, CLOSE CURSOR, COMMIT WORK, CONNECT, CREATE
    ASSERTION, CREATE CHARACTER SET, CREATE COLLATION, CREATE DOMAIN, CREATE
    ORDERING, CREATE ROLE, CREATE ROUTINE, CREATE SCHEMA, CREATE TABLE, CREATE
    TRANSFORM, CREATE TRANSLATION, CREATE TRIGGER, CREATE TYPE, CREATE VIEW,
    DECLARE CURSOR, DELETE CURSOR, DELETE WHERE, DISCONNECT, DROP ASSERTION, DROP
    CHARACTER SET, DROP COLLATION, DROP DOMAIN, DROP ORDERING, DROP ROLE, DROP
    ROUTINE, DROP SCHEMA, DROP TABLE, DROP TRANSFORM, DROP TRANSLATION, DROP
    TRIGGER, DROP TYPE, DROP VIEW, FETCH, FREE LOCATOR, GRANT, GRANT ROLE, HOLD
    LOCATOR, INSERT, OPEN, RELEASE SAVEPOINT, RETURN, REVOKE, ROLLBACK WORK,
    SAVEPOINT, SELECT, SET CONNECTION, SET CONSTRAINT, SET ROLE, SET SESSION
    AUTHORIZATION, SET SESSION CHARACTERISTICS, SET TIME ZONE, SET TRANSACTION,
    START TRANSACTION, UPDATE CURSOR, UPDATE WHERE.

STATEMENT INFORMATION ITEM
    The header part of a status record.

STATEMENT TERMINATOR
    A token in an SQL statement that marks statement end. Almost always a
    semicolon (;), but in embedded COBOL one would use END-EXEC. In some contexts
    the statement terminator may be omitted.

STATIC CURSOR
    An ODBC Term. A Cursor that is not dynamic. See also: DYNAMIC CURSOR.

STATIC SQL
    Statements in static SQL assume prior knowledge of the database structure,
    therefore no access is required to "descriptor areas" at runtime. As opposed
    to: dynamic SQL. Static SQL may be more efficient when a precompiler is used,
    since more information is known in advance. Static SQL statements are called
    "static" because they stay the same, instead of changing when the application
    runs. See also: DYNAMIC SQL.

STATUS CODE
    The value that is returned in SQLSTATE.

STATUS CONDITION
    The exception or completion condition that an SQL statement or CLI function
    causes to be raised. See also: status record.

STATUS PARAMETER
    See: SQLSTATE.

STATUS RECORD
    A CLI term. Inside the diagnostics area are zero or more status records. If
    present, a status record has information about an exception condition or
    completion condition that was detected during execution of the last CLI
    function. The record's main fields are: sqlstate string, native-error integer,
    implementation-dependent error message string. The ODBC manual uses the term
    "diagnostic record" rather than status record. The Standard uses the terms
    "condition" or "condition information item" rather than status record in some
    places, but uses the term status record when the context is the standard CLI.

STATUS VARIABLES
    The sqlcode integer and the sqlstate string.

STMT
    A CLI term. A structured area which is created by SQLAllocHandle
    (SQL_HANDLE_STMT,...), which is destroyed by
    SQLFreeHandle(SQL_HANDLE_STMT,...), which belongs to a dbc, which is
    referenced via a handle (the hstmt) and which is used by all CLI functions
    that have to do with "statements". The full standard term is actually
    "allocated SQL statement", but the abbreviations hstmt and hstmt are used in
    the Standard for CLI examples; we have preferred them because "SQL statement"
    usually means something else.

STORE
    To place (a value) within the DBMS's scope. Opposite of retrieve.

STORE ASSIGNMENT
    Assign to a target which can contain NULL (without needing a separate
    indicator parameter). For example: putting values from C parameters into rows
    in a Table.

STORED PROCEDURE
    A procedure which is kept in the database.

STRING
    [1] A C term. An array of characters ending with a null terminator.

    [2] An SQL term. A sequence of bits or characters. A value in a BIT or
    character Column. Or, in SQL3: also a value in a BINARY Column.

STRUCTURE
    A standard C term. A type of data object whose values are sequences of members
    that have other data object types.

STRUCTURED TYPE
    An Object/Relational term. A UDT which is not a distinct type. Structured
    types are the only data types which may be part of multi-member type families.
    Structured types are made with CREATE TYPE statements that contain at least
    one attribute definition or UNDER clause.

SUB (prefix)
    In general, one prefixes SUB to a word to indicate it "doesn't stand on its
    own" -- as in subclass, sublanguage, subquery, subtable, subtype. Sometimes it
    corresponds to a term with the prefix: super.

SUBCODE
    See: SUBTYPE.

SUBCLASS
    The last three characters of the 5-character status code (the first two
    letters are the Class).

SUBJECT DATA TYPE
    The data type in effect for a Column definition, which affects what can be in
    the DEFAULT clause.

SUBJECT ROUTINE
    An SQL3 term. The routine which is effectively called.

SUBJECT Table
    [1] The Table that a Trigger acts on.

    [2] The Table that a DELETE or UPDATE or INSERT statement acts on.

SUBLANGUAGE
    A language which does not stand on its own, because some constructs (e.g.:
    procedural loops) are not defined and therefore sublanguage statements must be
    somehow bound with a host language. Standard SQL-92 is in fact a sublanguage
    but traditionally it is called a language. With PSM the appropriate constructs
    exist, but PSM implementations are not common (yet).

SUBQUERY
    An SQL Standard term. A parenthesized query which is not an SQL statement. The
    common example is "SELECT * FROM Table_1 WHERE C1 IN (SELECT C2 FROM
    Table_2);", where the "(SELECT C2 FROM Table_2)" portion is a subquery and the
    "SELECT * FROM Table_1 ..." portion is sometimes informally called an outer or
    parent statement. In the statement "INSERT INTO Table_1 VALUES (1);" the
    "VALUES (1)" portion is not parenthesized and therefore not formally a
    subquery, but logically it certainly is. There are three types of subquery:
    scalar subquery, row subquery, Table subquery.

SUBTABLE
    An Object/Relational term.

    [1] A typed Table which is effectively subordinate to another Table (the
    "supertable"), in the same way that a subtype is subordinate to a supertype.
    Subtables are defined with CREATE TABLE <subtable name> OF <UDT name> UNDER
    <supertable name>, where: (a) the supertable is also a typed Table and (b) the
    subtable's UDT is a direct subtype of the supertable's UDT.

    [2] Similarly to [1], a "viewed subtable" or "subview" is a View which is
    created UNDER another Table.

    [3] In the same way that a set is its own subset, all Tables are subtables of
    themselves. See also: DIRECT, PROPER, SUBTYPE, UDT.

SUBTRANSACTION
    A non-standard term. The part of a transaction which lies between the
    transaction start and a given savepoint or between a given savepoint and
    "now".

SUBTYPE
    [1] An Object/Relational term. (In a UDT hierarchy) Type Chimp is a subtype of
    type Primate if it was created thus: "CREATE TYPE Chimp ... UNDER Primate
    ...". If in turn Primate is a subtype of Mammal, then Chimp is also a subtype
    of Mammal. In both cases, Chimp is a "proper subtype". Since Chimp may inherit
    attributes or methods from Primate (the supertype), subtypes formed this way
    are sometimes called "extensions" (of the supertype).

    [2] (Of any data type) In the same way that every set is a subset of itself,
    every data type is its own subtype. For example: INTEGER is a subtype of
    INTEGER (and of nothing else) and Chimp is a subtype of Chimp (among other
    things). In these two examples, neither INTEGER nor Chimp are "proper
    subtypes".

    [3] (A common erroneous definition) "A data type T2 is a subtype of data type
    T1 if every value of T2 is also a value of T1". Unfortunately this definition
    suggests that SMALLINT is a subtype of INTEGER, which isn't so: no predefined
    data type is a subtype of anything except itself. See also: PROPER SUBTYPE,
    DIRECT SUBTYPE, SUPERTYPE.

    [4] Also known as: subcode or DATETIME_INTERVAL_CODE or datetime data type. A
    numeric code which is used in conjunction with the SQL data type code, for
    datetime and interval data types only. If SQL data type code = 9 (datetime)
    then subtype = 1 (date) or 2 (time) or 3 (timestamp) or 4 (time with time
    zone) or 5 (timestamp with time zone). If SQL data type code = 10 (interval)
    then subtype = 1 (year) or 2 (month) or 3 (day) or 4 (hour) or 5 (minute) or 6
    (second) or 7 (year to month) or 8 (day to hour) or 9 (day to minute) or 10
    (day to second) or 11 (hour to minute) or 12 (hour to second) or 13 (minute to
    second).

SUBVERT
    Don't use this word, use "violate" instead.

SUBVIEW
    An Object/Relational term. A View which is a subtable.

SUCCESS
    The "okay" state. An SQL/CLI function returns SQL_SUCCESS in the return code
    if there are no errors or warnings.

SUMMARY QUERY
    Infrequent term. A SELECT statement which contains any or all of (a GROUP BY
    clause) (a HAVING clause) (a set function).

SUPER KEY
    A candidate key containing more Columns than are necessary for ensuring
    uniqueness.

SUPERTABLE
    An Object/Relational term. "Supertable" is defined as the reverse of
    "subtable", that is, if Table t1 is a subtable of Table t2, then t2 is a
    supertable of t1.

SUPERTYPE
    An Object/Relational term. "Supertype" is defined as the reverse of "subtype",
    that is, if type t1 is a subtype of type t2, then t2 is a supertype of t1.

SYBASE
    A vendor. Makes "Adaptive Server Enterprise" (formerly Sybase SQL Server) and
    "Adaptive Server Anywhere" (formerly Watcom SQL). www.sybase.com.

SYNONYM
    A DB2/Oracle term. A Schema Object which translates one Table name to another.
    In standard SQL one might use a View for this purpose.

SYNTAX
    The expected order and significance of keywords in a language.

SYNTAX RULE
    An SQL Standard term. A syntax rule declares not only what the correct way to
    express an SQL statement is, but also what Objects must be present (therefore
    a "syntax error" exception condition may be the result of either syntax error
    or Catalog lookup failure). See also: ACCESS RULE, GENERAL RULE.

SYSTEM
    From the Greek for "put together". A large computer software package with
    several distinguishable program components. Common examples: "operating
    system", "database management system". In the Standard, the word system
    usually seems to mean operating system.

SYSTEM CATALOG
    Obsolete for metadata or INFORMATION_SCHEMA.

SYSTEM GENERATED
    An Object/Relational term.

    (Of a self-referencing Column) Values are assigned by the DBMS during insert
    -- opposed to "user-generated" or "derived" values.

SYSTEM R
    An early IBM relational DBMS, a precursor of SQL. See also: SEQUEL.

SYSTEM_USER
    An SQL niladic character function, which returns an implementation-defined
    string that equals what the operating system thinks your name is (as opposed
    to what you logged in to the DBMS with when you connected, which is
    SESSION_USER).

T
-

TABLE
    [1] An Object defined by a CREATE TABLE statement, which contains one or more
    ordered Columns.

    [2] An instance of the preceding, after INSERTs happen, containing one or more
    unordered rows.

    [3] (deprecated) A file. Called "Table" because its conceptual representation
    is a vertical bunch of Columns and a horizontal bunch of rows.

TABLE CONSTRUCTOR
    See: TABLE VALUE CONSTRUCTOR.

TABLE ELEMENT
    A Column or Constraint definition within the CREATE TABLE or ALTER TABLE
    statements.

TABLE EXPRESSION
    [1] An SQL Standard term. This is the BNF: "FROM clause [WHERE clause] [GROUP
    BY clause] [HAVING clause]". Notice that a Table expression does not include a
    select list or an ORDER BY clause.

    [2] (in the writings of C.J.Date) A synonym for what the Standard calls a
    query expression.

TABLE OPERATOR
    A FIPS term. One of the operators that combines queries: UNION or EXCEPT or
    INTERSECT. We prefer the Standard's term: set operator.

TABLE REFERENCE
    [1] One of the comma-delimited references in a FROM clause. Usually that's
    just the Table identifier, as in "FROM t1,t2" or "FROM Schema1.Table1".
    Sometimes there's a Correlation name attached, as in "FROM Table_1 AS t1,
    Table_2 AS t2". Sometimes there's a nested Table, as in "FROM (SELECT * FROM
    Table_1) AS t1".

TABLE SUBQUERY
    A subquery which returns (potentially) more than one row and (probably) more
    than one Column). See also: NESTED TABLE.

TABLE VALUE CONSTRUCTOR
    Also: table constructor. A query expression formed with "VALUES (row-value
    expression) [,(row-value expression)...]". In effect: you can build a
    multi-Column multi-row Table into an SQL statement. Not that you'd want to
    though. Table value constructors are occasionally used for static multi-row
    INSERTs.

TABLESPACE
    DB2/Oracle term. A section of a disk reserved for physical storage of a Table.
    Advanced users can define two or more Tables in the same Tablespace. With
    MS-DOS / Windows, tablespace means file, but sometimes a BLOB is not in the
    same file as the rest of the fields.

TARGET SPECIFICATION
    Where to place (target) output from an SQL statement. The target specification
    is an output host variable. In the CLI, descriptions of target specifications
    are in the ARD. See also: SIMPLE TARGET SPECIFICATION.

TAUTOLOGY
    A search condition which can be guaranteed to return TRUE, for example "1 =
    1".

TECHNICAL CORRIGENDUM
    See: CORRIGENDUM.

TEMPORAL
    Having to do with time. The SQL temporal data types are the datetime data
    types (DATE/TIME/TIMESTAMP) plus INTERVAL.

TEMPORARY
    Adjective. When a Base table is TEMPORARY, the values in all rows disappear
    when the transaction or session ends. In SQL3, a View can also be TEMPORARY.

TENTATIVELY
    Not an SQL Standard term. We used it in descriptions of data change operations
    as a reminder that any changes are still subject to reversal due to a
    ROLLBACK. Data changes are not permanent until COMMIT happens.

TERMINAL
    The end of the trail. A terminal node has lines coming in but none going out.
    In BNF, a terminal is a keyword or a special character used as an operator and
    it is combinations of terminals which we use to construct non-terminal
    expressions.

TERMINATOR
    An embedded SQL term. The mark that ends an SQL statement. The mark differs
    depending on the host language. In C or Pascal: semicolon. In COBOL: END-EXEC.

TERNARY RELATION
    A relation with three Columns.

THETA JOIN
    A relational term. A join based on any comparison operator. A specific case,
    where the operator is =, is an Equijoin.

THIRD NORMAL FORM
    A relational term. A Table is in third normal form if no Column functionally
    depends on a Column which is not part of the primary key. For example: if
    country='UK' then monarch='Queen Elizabeth II' and heir='Prince Charles'. That
    is, monarch and heir are both functionally dependent on country. But heir also
    depends on monarch (because if the Stuarts overthrow the Queen then the Prince
    changes too). Therefore "CREATE TABLE Kingdoms (country ... PRIMARY KEY,
    monarch ..., heir ...)" does not describe a Table which is in third normal
    form.

THREE-VALUED LOGIC
    A system which contains three logical values: TRUE or FALSE or UNKNOWN. Since
    SQL allows three-valued logic while most procedure languages allow only
    two-valued (TRUE/FALSE) logic, this is a source of occasional confusion.
    Usually the UNKNOWN value happens because NULLs are present somewhere.

TIME
    One of the basic data types. Represents time of day with a 24-hour clock. An
    example of a TIME literal is '12:00:00'.

TIME ZONE
    Since the sun is not in the same position of the sky at the same time for all
    regions of the round earth, the time of day differs depending on longitude,
    that is, the distance east or west of the zero meridian (Greenwich). In SQL we
    take this factor into account with the two data types: TIME WITH TIME ZONE and
    TIMESTAMP WITH TIME ZONE.

TIMEOUT
    An ODBC term. A timeout is a connection or statement attribute which is an
    integer, containing the number of seconds which should elapse before the DBMS
    gives up and returns an error: "Operation timed out".

TIMESTAMP
    [1] An SQL Standard term. One of the basic data types. Represents both date
    and time of day, that is, TIMESTAMP is a combination of a DATE and a TIME. An
    example of a TIMESTAMP literal is '2000-01-01 00:00:00'.

    [2] A SQL Server term. A TIMESTAMP data type is a binary sequence number used
    to order statement execution -- the date+time data type is DATETIME. We never
    use this meaning.

TIMESTAMPING
    An optimistic concurrency control, which requires each accessed/updated row to
    be marked with a timestamp, which may be some arbitrary serial number or a
    precise time of day.

TOKEN
    An SQL Standard term. A parser breaks up an SQL statement up into its minimal
    syntactic components and throws away comments or separators. The result is
    individual tokens. For example ``"SELECT /* comment */ col1, 'X' FROM Table_1``
    becomes 5 tokens: <SELECT> <col1> <'X'> <FROM> <Table_1>.

TRACE FILE
    An ODBC term. For audit or debugging purposes, you may choose to have copies
    of every SQL statement printed to a file. That file is called the trace file.
    See also: JOURNAL, LOG.

TRAILING
    Appearing at the end of a string. Opposite of leading. In the character string
    'ABC ' there is one trailing space. Use this word instead of "rightmost"
    because (e.g.:) Arabs write from right to left.

TRANSACTION
    Also SQL-transaction.

    [1] All activities which have taken place since the last COMMIT or ROLLBACK.

    [2] A group of SQL procedure statements which constitute an atomic execution
    unit, i.e.: must either all succeed together or all fail together.

TRANSACTION STATEMENT
    Also SQL-transaction statement. One of: COMMIT, ROLLBACK, SET CONSTRAINTS, SET
    TRANSACTION. In SQL3, add: START TRANSACTION, SAVEPOINT, RELEASE SAVEPOINT.

TRANSFORM
    An SQL3 term. A function which is automatically called when a UDT value is
    output from the DBMS to the application or input from the application to the
    DBMS. There is a CREATE TRANSFORM and a DROP TRANSFORM statement.

TRANSIENT
    Designed to have a short existence. SQL-sessions and SQL statements are
    transient, but the things they operate on -- Modules and databases -- are
    persistent. See also: TEMPORARY.

TRANSLATE
    An SQL function which changes a string from Character set X to Character set
    Y. This may involve transliteration, e.g.: change Latin KHAN to Cyrillic XAH
    (notice that 4 Latin characters became 3 Cyrillic characters --
    transliteration is rarely one-to-one character-to-character). It may also
    may involve whatever the implementor wants.

TRANSLATION
    A named SQL Object which controls the mapping between two Character sets. Used
    by the TRANSLATE function.

TRANSLATOR DLL
    An ODBC term. A DLL which is used to convert character strings to and from the
    default Windows code page. This is necessary if the application or DBMS does
    not support SQL-92 Character sets.

TRIADIC
    Having three operands or parameters and so distinguishable from niladic,
    monadic and dyadic. BETWEEN is a triadic operator. SUBSTRING is a triadic
    function.

TRIGGER
    An SQL3 term. A named Schema Object, associated with a Base table, which
    describes a Trigger action time (BEFORE or AFTER), a Trigger event (INSERT or
    UPDATE or DELETE) and a Trigger action (one or more SQL procedure statements).
    When the event happens, the DBMS executes the Trigger action. See also:
    CONSTRAINT.

TRIGRAPH
    An SQL3 term. A three-character string which can be used as a substitute for a
    bracket. SQL's left bracket trigraph is ??(. SQL's right bracket trigraph is
    ??).

TRIM
    An SQL function which removes lead or trail pad characters. Usually the pad
    character is a space.

TRUE
    One of the BOOLEAN values (the other two are FALSE and UNKNOWN). See also:
    LOGIC, THREE-VALUED LOGIC, BOOLEAN.

TRUNCATION
    [1] Chopping of trailing characters in a character string or the trailing bits
    in a bit string. Happens automatically when assigning a CHAR(6) string to a
    CHAR(5) string. Also happens with TRIM.

    [2] Chopping of post-decimal digits in a number (as opposed to rounding).

    [3] Oracle term. Deletion of all rows in a Table.

TUPLE
    Relational term. See: ROW, RELATION.

TWO-PHASE COMMIT
    When a single transaction is being processed by more than one server, there is
    a danger that the "all-or-nothing" requirement of the COMMIT process will be
    violated: one server fails, the other succeeds. Two-phase commit will first do
    the transaction, then check that it was done.

TYPE
    [1] A verb whose modifier indicates whether a computer language is strict
    about data type definitions; thus BASIC is "weakly typed" but Pascal and the
    modern versions of SQL are "strongly typed".

    [2] See: DATA TYPE.

TYPE INDICATOR
    An ODBC term. An integer representing a data type. For example, the CHAR data
    type is associated with the code value 1. See also: DATA TYPE CODE.

TYPE-PRESERVING FUNCTION
    A function whose input and output have the same data type. Specifically: if
    the input parameter has declared type "t", then the return value has most
    specific type "t" or a subtype of "t".

TYPED TABLE
    An Object/Relational term. A Base table which is created with CREATE TABLE
    <Table name> OF TYPE <UDT name>, where <UDT name> refers to a structured
    instantiable UDT. Or, a View which is created similarly. The first Column in a
    typed Table is a self-referencing Column, hence typed Tables are often called
    "referenceable Tables". The other Columns in a typed Table have names and data
    types which correspond to the names and data types in the UDT's attribute
    definitions. See also: SELF-REFERENCING COLUMN.

U
-

UNBIND
    [1] In an IDA of an ARD, set the SQL_DATA_POINTER field to zero. Or, set all
    SQL_DATA_POINTER fields to zero by calling SQLFreeStmt(SQL_UNBIND).

    [2] In an IDA of an APD, set the SQL_DATA_POINTER field to zero. Or, set all
    SQL_DATA_POINTER fields to zero by calling SQLFreeStmt(SQL_RESET_PARAMS).

UDT
    An SQL3 term. Abbreviation for User Defined Type: a data type which is created
    by the user with a CREATE TYPE statement. In SQL3 you can go beyond the
    predefined data types such as INTERVAL and FLOAT and define your own data
    types. But there's lots of work: you must define processes for every operation
    that values of this data type can undergo. UDTs are Schema Objects in the same
    name space as Domains; they contain components (attributes or methods); they
    may be used wherever a data type" is called for; they are analogous to what in
    OO jargon is called a "class": they have some object-orientation features such
    as inheritance and constructors. The two kinds of UDT are: Distinct Type,
    Structured Type. See also: ADT, DOMAIN.

UNDER
    An Object/Relational term.

    [1] A clause in a CREATE TABLE or CREATE VIEW statement, which allows for
    creation of subtables.

    [2] A clause in a CREATE TYPE statement, which allows for creation of
    subtypes.

    [3] A Privilege to use an UNDER clause for an Object (Table or UDT), required
    when defining subtypes or subtables.

UNDERLINE
    See: UNDERSCORE.

UNDERLYING
    Used as a foundation in an Object definition. Example: if we say "CREATE VIEW
    V (v1) AS SELECT s1 FROM Table_1;", then Table_1 is the underlying Table of
    View V and s1 is the underlying Column of View Column v1.

UNDERSCORE
    The _ character (value = 95 in ISO 8859-1 encoding). Underscores may be used
    inside identifiers. They operate as position markers within LIKE patterns.

UNICODE
    [1] A standardized encoding which takes into account the great majority of the
    world's writing schemes. There are several levels, but what most people mean
    when they say "Unicode" is: a 16-bit "wide char" encoding which matches
    official standard ISO 10646. Text: The Unicode Consortium, The Unicode
    Standard, Version 2.0, 1996. ISBN 0-201-48345-9. Web site: www.unicode.org.

    [2] In SQL3, a predefined Character set. It may also be called ISO10646. This
    set includes all Unicode characters. It may be the same set as SQL_TEXT.

UNION
    One of the SQL set operators (the others are EXCEPT and INTERSECT). The union
    of a set containing {a,b,c,d,e} with a set containing {c,d,e,f,g} results in
    {a,b,c,d,e,f,g} (duplicates are eliminated). If the operator is UNION ALL, the
    result is {a,b,c,c,d,d,e,e,f,g} (duplicates are not eliminated).

UNION COMPATIBLE
    Having the same degree (number of Columns) and having similar Columns. Thus
    (5,'A') is union compatible with (-33,'C') but not with ('A',5) or (5).

USER DESC
    A desc which is created with SQLAllocHandle(SQL_HANDLE_DESC...) and associated
    with a dbc. As opposed to: automatic desc.

UNION JOIN
    An operation which combines the features of a union and a join.

UNIQUE
    (Of a set) All members of the set have different values. A NULL is different
    from another NULL. A non-NULL is different from another non-NULL if a
    comparison shows they're not "equal". For example, the following set is
    unique: {1,2,3,4,NULL,NULL}. For counter-example, the following set is not
    unique: {1,2,3,4,4,NULL,NULL}. The search condition "UNIQUE (SELECT col1 FROM
    Table_1);" is TRUE if the subquery is unique. The Table Constraint in "ALTER
    TABLE Table_1 ADD CONSTRAINT c UNIQUE (col1);" is satisfied if Table_1 is
    unique.

UNIQUE INDEX
    An index whose keys must be unique. Often unique indexes are used to support
    the UNIQUE Constraint, but that's an implementation consideration -- index
    usage is not defined by the SQL Standard.

UNIT OF WORK
    Non-standard term. See: TRANSACTION.

UNIVERSAL TIME
    See: UTC.

UNIX
    An operating system.

UNKNOWN
    One of three logical-result values (the others are the more familiar TRUE and
    FALSE). See also: LOGIC.

UNNAMED
    [1] (Of a Column) The statement "SELECT Column_1, 1+1 AS "1+1",
    UPPER(Column_2) FROM Table_1;" has 3 Columns in a select list. The first is
    named: it inherits the Table Column name. The second is named: it has an AS
    clause. The third is unnamed: although the DBMS will assign it an
    implementation-dependent name, it's not explicitly named.

    [2] (Of a Module) Lacking a name clause.

UNQUOTED
    (Of a string) Not within quotes. 'A' is a quoted string; A is an unquoted
    string.

UPDATABLE
    An SQL Standard term. Applies to query expressions and therefore applies to
    Views (since in the Standard definition a View is a named query expression).
    The phrase "updatable View" is common. Updatability is certain if the query
    merely selects some or all Columns from one Base table; beyond that
    restrictions may apply. An updatable View can be used as the object of INSERT,
    UPDATE or DELETE operations.

UPDATE
    [1] An SQL keyword, found at the start of an "UPDATE statement", which changes
    specified Column values in existing rows. Example: "UPDATE Employees SET
    salary = salary / 2;".

    [2] (When set in lower case to indicate it is not a keyword) Change database
    contents with any or all of: DELETE, INSERT, UPDATE.
    But see: DATA CHANGE STATEMENT. Note that some other SQL statements, such as
    DROP and ALTER, may have an implicit updating effect.

UPDATE RULE
    The part of a Constraint clause that begins with the words "ON UPDATE ...".
    This specifies referential action on a foreign key if a primary key is
    updated.

UPPER
    An SQL monadic function which returns the upper-case equivalent of a character
    string. Thus UPPER('A. Smith') returns 'A. SMITH'. In SQL-92 the UPPER
    function only works for simple Latin letters, in SQL3 the UPPER function
    should work for any letters.

UPPER CASE
    A form of a letter in a Latin, Greek, Cyrillic, Georgian or Armenian alphabet.
    In English text, upper case is used at the beginning of a sentence or proper
    name. The official (Unicode) name of an upper case letter always contains the
    word "capital", e.g.: LATIN CAPITAL LETTER M.

USAGE
    An SQL Standard term. A type of Privilege which applies to non-tabular
    Objects, such as Domains or Translations.

USER
    [1] Somebody who types on a keyboard or clicks on a mouse.

    [2] The person(s) associated with an AuthorizationID. See also: ROLE.

USER DEFINED TYPE
    See: UDT.

USER IDENTIFIER
    [1] (SQL-session user identifier) An identifier which is set by the CONNECT or
    (SQL3) SET SESSION AUTHORIZATION statement and is retrievable via the
    SESSION_USER niladic function.

    [2] (Current user identifier) An identifier which may be the same as the
    session user identifier, but with SQL3 the authorization might be a Role
    instead.

USER TABLES
    Tables that users can CREATE and DROP. The Views in INFORMATION_SCHEMA are not
    user Tables.

USER-DEFINED
    The opposite of implementation-defined. In SQL3, users can define certain
    things (such as data types and functions) which are fixed ("built in") with
    earlier versions of the SQL Standard.

USER-DEFINED TYPE
    See: UDT.

USER GENERATED
    An Object/Relational term.

    (Of a self-referencing Column) Values are supplied by the user during insert
    -- as opposed to "system generated" or "derived".

UTC
    Stands for Universal Time Coordinated (though many people prefer to say
    Universal Coordinated Time). The base for displacement of SQL time values.
    Differs by a few seconds from GMT (Greenwich Mean Time).

V
-

VALID
    Legally acceptable. Said of a value, a database state, a locator, a character
    encoding, a procedure or an identifier.

VALIDATION
    [1] Obsolete for Constraint (on a Column).

    [2] Syntax check to determine whether a literal value is appropriate for a
    data type, for example whether '199x-44-12' is a valid date.

    [2] An ODBC term. A comparison of a parsed statement's identifier tokens
    (e.g.: Table names) with the database Catalog components (e.g.: Table
    descriptors), accompanied by Privilege testing.

VALUE
    SQL distinguishes between "row values" (multi-component) and "scalar values"
    (single-component). In this book we sometimes use value as a synonym for
    scalar value.

    [1] An occurrence of an attribute. For example: color is an attribute and
    "green" is a specific color, so "green" is an occurrence of a color attribute.

    [2] A literal or expression result. To remember the distinction between a
    variable and its value, pull a penny out of your pocket. Read it. It says "One
    Cent" on one side. But you did not pull out one cent. You pulled out one
    penny.

VALUE SPECIFICATION
    A value by itself, with no operators. Thus these are value specifications: a
    literal, a host variable (including indicator), a Column name, a niladic
    function, the word VALUE in a Domain Constraint. If you put two value
    specifications together, e.g.: 5+5, that's a value expression. See also:
    SIMPLE VALUE SPECIFICATION.

VALUES
    An SQL-92 verb. Most commonly seen nested in an INSERT statement, as in
    "INSERT INTO Table_1 VALUES (1,2,3);".

VARCHAR
    An abbreviation for CHAR VARYING. See: CHARACTER, VARYING.

VARIABLE
    [1] Any unknown in an equation -- e.g.: for "x+5", x is a variable (5 is a
    constant or literal).

    [2] See: HOST VARIABLE.

    [3] See: PARAMETER.

VARIABLE-LENGTH
    See: VARYING.

VARIABLE-LENGTH ENCODING
    An encoding, popular for Chinese and Japanese character sets, where one, two,
    or more octets may be needed to represent a character. Usually variable-length
    encoding involves escape sequences. See also: FIXED-LENGTH ENCODING,
    FORM-OF-USE, MULTIBYTE.

VARYING
    (Of a CHAR or BIT description) Variable in length. Thus, a Column described as
    BIT VARYING (n) may contain values whose length ranges from 0 to n bits.
    Similarly, a Column defined as CHAR VARYING (5) might contain 'ABCDE' (4
    characters) or only 'A ' (2 characters). It is not correct to say that a CHAR
    VARYING is a CHAR from which trail spaces are stripped. An abbreviation for
    CHAR VARYING is VARCHAR. For the opposite, see: FIXED-LENGTH.

VENDOR
    A certain company who sells an SQL product. See also: IMPLEMENTOR. In this
    book, we have used "implementor" as a vague term when we had nobody particular
    in mind; we have used "vendor" to mean, specifically, one of these companies:
    {Centura IBM Informix Ingres Inprise Microsoft Ocelot Oracle Sybase XDB}.

VERB
    Not an SQL Standard term. An SQL keyword, generally the first word in an SQL
    statement, often an English verb, which describes the general action. For
    example: SET, SELECT, CREATE. See also: STATEMENT IDENTIFIER.

VERBOSE CODE
    An ODBC term. For this book we have preferred the standard term: see DATA TYPE
    CODE.

VERSION
    A non-standard term. Part of the definition of the implementation. In
    SQLGetInfo, this is a string containing '##.##.#### comment', where the first
    two digits are the major version, then comes the minor version, then the
    release and then an optional comment or name.

VERSIONING
    An ODBC term. A non-standard aid for concurrency control.

VIEW
    [1] An SQL Standard term. According to the Standard a View is a "named query"
    in a Schema, defined with a CREATE VIEW statement. So, very pickily: a View is
    not a Table. But the result of a View is a Table. That is why one sometimes
    sees the term "Viewed Table".

    [2] Also derived Table or virtual Table. A Table whose definition and content
    come from another Table via a selection. (Do not use "View" in this sense --
    only named derived Tables should be called Views.)

VIEW COLUMN LIST
    The list of Column names that optionally appears in a View definition. In
    "CREATE VIEW V (v1,v2) AS SELECT t1,t2 FROM Table_1;" the list (v1,v2) is a
    View Column list.

VIEW DEFINITION
    A CREATE VIEW statement.

VIEWED TABLE
    See: VIEW.

VIOLATE
    Fail or refuse to comply with a rule or convention. Example: if we have a
    Domain Constraint "CHECK (value > 6)" and we say "INSERT ... VALUES (5)", we
    are attempting to violate the Constraint. One can also attempt to violate
    security (by getting around the Privilege restrictions).

VIRTUAL COLUMN
    A dBASE term. A Column which is based on a calculation, as opposed to a Column
    which is actually stored in the Base table. See also: PSEUDO-COLUMN.

VIRTUAL TABLE
    A Table which is derived from another Table (or Tables) via the application of
    relational operators. For example: "SELECT a,b,c FROM Table_1 WHERE a=5;"
    brings three virtual Tables into momentary existence: (1) "FROM Table_1" makes
    a virtual Table which is a copy of the Base table t; (2) "WHERE a=5" makes a
    virtual Table which is a row-subset (i.e.: restriction) of the Table made by
    step (1); (3) "SELECT a,b,c" makes a virtual Table which is a projection of
    the Table made by step (2). Usually these "virtual Tables" are only
    conceptual, but it helps us understand SQL syntax if we realize that every
    SELECT clause makes a virtual Table. For non-virtual Tables, see: BASE TABLE.
    For named virtual Tables, see: VIEW. For virtual Tables which are
    materialized, see: DERIVED TABLE.

W

WARNING
    An SQL procedure statement can end with success, no-data, error or warning.
    The SQLSTATE variable will get a status code with class = '01'. If the
    statement was executed via a CLI function call, the return code will be
    SQL_SUCCESS_WITH_INFO. Typically a warning happens if the statement executed,
    but something was noticed during execution. For example: "NULL value
    eliminated during set function". See also: COMPLETION CONDITION.

WATCOM SQL
    See: SYBASE.

WHENEVER
    The embedded SQL statement "EXEC SQL WHENEVER SQLERROR GOTO x;" means: "after
    every SQL statement following this, there is an implicit host language
    statement saying "if (sqlcode<0) goto x;".

WHERE CLAUSE
    A clause which contains a search condition. The WHERE clause picks out those
    rows for which the search condition is TRUE (not FALSE or UNKNOWN).

WHILE
    A PSM term. A keyword introducing a "while statement", which takes the form:
    [<label> :] WHILE <search condition> DO <SQL statement list> END WHILE
    [<ending label>]. See also: FOR, LOOP, REPEAT.

WHITE SPACE
    One or more spaces or characters which SQL considers to be equivalent to
    spaces for the purpose of deciding "this is a separator" (as opposed to: part
    of a token). The following are the white space characters in Unicode, with
    hexadecimal codes (notice that the first seven are also in the ASCII_FULL
    Character set): Horizontal Tab (U+0009), Line Feed (U+000A), Vertical
    Tabulation (U+000B), Form Feed (U+000C), Carriage Return (U+000D), Space
    (U+0020), No-Break Space (U+00A0), En Quad (U+2000), Em Quad (U+2001), En
    Space (U+2002), Em Space (U+2003), Three-Per-Em Space (U+2004), Four-Per-Em
    Space (U+2005), Six-Per-Em Space (U+2006), Figure Space (U+2007), Punctuation
    Space (U+2008), Thin Space (U+2009), Hair Space (U+200A), Zero Width Space
    (U+200B), Zero Width Non-Joiner (U+200C), Zero Width Joiner (U+200D),
    Left-To-Right Mark (U+200F), Right-To-Left Mark (U+200F), Line Separator
    (U+2028), Paragraph Separator (U+2029), Zero Width No-Break Space (U+FEFF).

WIDE CHAR
    A C term. A 16-bit character encoding which is signalled by the type
    definition char_t and whose strings are preceded by L as in L"abc". See also:
    ENCODING, MULTIBYTE, UNICODE.

WILDCARD
    A special "stands for anything" character in a LIKE or SIMILAR pattern,
    usually % or _.

WRITE
    An operating system term. The word "write" usually applies to disk files: by
    writing a record, we make a copy of that record in a disk file. For a database
    context, this would usually occur if we COMMIT after a data-change. See also:
    READ.

WRITE-AHEAD CACHE
    An operating system term. An area in RAM which holds copies of buffers that
    should be written to disk. Write-ahead caches increase speed but (if the
    operating system is MS-Windows) they are unsafe.

X
-

X/OPEN
    "X/Open and the 'X' symbol are registered trademarks of X/Open Company Ltd. in
    the UK and other countries" ... This organization, which is involved with
    several Unix standards, published the Common Applications Environment (CAE)
    specification, with the SAG/CLI. X/Open's "Data Management Working Group" is
    responsible for a standard that is much like ISO Standard SQL Intermediate
    Level, plus a few commands which many vendors have implemented (like CREATE
    INDEX and DROP INDEX). X/Open is now part of The Open Group, www.open.org.

X3
    The American ACME which is responsible for some computer standards. Above X3
    is ANSI. Below X3 are the technical committees, of which the most relevant is
    X3H2, the members of which discuss and propose the wording of one particular
    standard: SQL. In other words, the SQL Standard is produced by the X3H2
    "Database" committee of the X3 organization, which reports to ANSI. See also:
    ISO.

Y
-

YEAR-MONTH INTERVAL
    An interval which includes year and/or month fields. See also: DAY-TIME
    INTERVAL.

Z

ZERO BASED INDEXING
    An ODBC term. In the C expression "a[n]", n is the index of an array. What is
    the first element of the array? If a[0], that's zero based indexing. In almost
    all SQL contexts, a[1] is the first element. However, there are some
    exceptions in ODBC.

ZONE
    See: TIME ZONE.

``[]``
    Non-standard special characters. Usual name: "brackets". Not used in standard
    SQL, but in syntax descriptions, brackets enclose options. See also: BNF.

``_``
    SQL special character; used as an introducer or as part of a name. Standard
    name: "underscore". The specification that the underscore is a SQL special
    character may be an error in the Standard. Underscores are often used in
    identifiers, for example: Time_Of_Day. They have a special significance in
    LIKE patterns, for example: "... LIKE '_A_B%' ...".

``|``
    SQL special character; used in a SIMILAR pattern to denote logical OR.
    Standard name: "vertical bar". Also called "broken vertical bar" or (in
    Unicode) "vertical line". In BNF, a vertical bar separates two options --
    e.g.: CASCADE | RESTRICT. See also: BNF.

``||``
    SQL concatenation operator. See also: CONCATENATION.

``{}``
    Non-standard special characters. Usual name: "braces". Also called (in
    Unicode) "curly bracket".

    [1] Not used in standard SQL, but in syntax descriptions braces enclose a
    choice of compulsory alternatives. See also: BNF.

    [2] In set-theory notation, braces enclose the members of a set. In this book
    we have used braces for both meaning [1] and meaning [2].
