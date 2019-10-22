.. highlight:: text

====================================
Appendix A -- Remote Database Access
====================================

Remote Database Access (RDA) is a standard for interfacing to databases via
some network. The standards for networks are usually bound up with a hierarchy
called the Open Systems Interconnect (OSI) layers, which look like this:

::

    LAYERS (from top to bottom) WHAT'S DEFINED

    ---------------             the programs the end-users see
    - Application -
    ---------------

    ----------------            negotiating syntax of messages
    - Presentation -
    ----------------

    ----------------            naming, session establishment
    - Session      -
    ----------------

    ----------------            acknowledgments, sequence numbers, time-outs
    - Transport    -
    ----------------

    ----------------            routing through network addresses
    - Network      -
    ----------------

    ----------------            packet structure
    - Datalink     -
    ----------------

    ----------------            bit stream, transmission rate
    - Physical     -
    ----------------

Typically, a DBMS programmer worries about Application, the top layer. RDA is
a specification for the next lower layers -- Presentation and Session. In
other words: END USERS AND APPLICATION PROGRAMMERS HAVE NO DIRECT INTEREST IN
RDA BECAUSE IT CONCERNS LOW-LEVEL CODING. Typically, the DBMS vendor supplies
some mediating software which covers or obscures the network communication
job.

All right: for most people, it's not vital to understand RDA in any detail.
What we think is useful is a short summary and tutorial. From this chapter,
you'll get an idea of:

* What RDA's job is.

* What sort of information goes back and forth on the network.

* What "client/server" actually means.

.. rubric:: Table of Contents

.. contents::
    :local:

ISO/IEC 9759
------------

The standard for RDA is ISO/IEC 9759 "Remote Database Access For SQL". This is 
a completely different document from the standard SQL document (ISO/IEC 9075), 
so it's not correct to say that RDA is part of the SQL standard. But it's a 
related standard, and the respective committees work together closely. 

Much of the impetus for RDA came from an industry consortium known as the SQL 
Access Group (SAG). In 1991 members of the SAG consortium produced the first 
prototypes for version 1 of RDA. The latest edition is Version 3, which is 
still unofficial at the time we're writing this. Version 3 is quite different 
from the earlier versions. It operates very much like the SQL/CLI 
specification, using similar or even the same names and parameters for most of 
its functions. For example, the SQL/CLI function ``SQLExecDirect`` has an RDA 
equivalent: ``RDAExecDirect``. The parameters are similar (a handle and a 
string with an SQL statement and a size word). The effect is similar (an SQL 
statement is parsed and executed). The big difference, and the whole point of 
RDA, is architecture: ``SQLExecDirect`` is a function which you call directly, 
``RDAExecDirect`` is a message which you pass to a "remote" entity. 

The nearby functions are the "client", the messages they send out are called 
"requests". The remote entity is the "server", the messages that it sends back 
are called "responses". 

TCP/IP
------

In the early RDA versions, the main concern was to interface via OSI. The
latest version is quite specific: the main transport layer should be
Transaction Connect Protocol / Internet Protocol, or TCP/IP. Actually TCP/IP
is a family of protocols, made famous by the fact that The Internet runs on
TCP/IP.

The TCP/IP protocol family is primarily responsible for the level "below" RDA
-- the Transport Layer. And, TCP/IP interfaces in its turn with the lower
levels. The OSI stack works like a bucket brigade: the top level sends buckets
down to the next level which passes to the next level and so on; meanwhile,
buckets are coming back the other way. Which buckets are empty or full,
depends on where the fire is at the moment.

The RDA is what's between you (the application) and TCP/IP (the transport).

The Client/Server Model
-----------------------

The client sends requests to the server. The server sends responses to the
client.

::

    client ----------requests------------->
         <---------responses-------------   server

There are only eleven RDA requests. Each request designates a distinct
operation that the client wants the server to perform. Here's the list:

::

    Request                  What the client wants the server to perform
    RDAConnect               Set up connection between client and server
    RDADisconnect            Cancel the connection made with RDAConnect
    RDAEndTran               COMMIT, ROLLBACK, or "prepare for COMMIT"
    RDAClientAttribute       Note what client's resource attributes are
    RDAStatementPrepare      Prepare an SQL statement
    RDAStatementDeallocate   Unprepare, close Cursor, free statement resource
    RDAStatementExecute      Execute a prepared SQL statement
    RDAStatementExecDirect   Prepare and execute a SQL statement in one go
    RDAStatementFetchRows    FETCH selected rows and send contents to client
    RDAStatementCloseCursor  No more selected rows will be fetched, clean up
    RDAStatementCancel       Cancel any of the "RDAStatement..." requests

There is only one RDA response. A response designates the results of a
server's performance -- or attempted performance -- of a client request.
Here's the list:

::

    Response                 What client should do with the response
    "RDAResponse"            Read diagnostics and/or fetched row values

The eleven requests, and the response are described below. You may assume that
all the messages contain identifiers and handles which are necessary to
synchronize operations. We have omitted such "protocol" information in our
descriptions. We have included only the "parameter" information, which is
necessary to illustrate the essential point of each particular operation.

RDAConnect
..........

**Message Content:**

::

    DestinationServerName character string       name of server
    UserName              character string       name of server
    Authentication        character string       name of server

**What the server is supposed to do:**

Answer the phone! The client is sending enough information for the server to
set up a connection -- notice that the parameters here are the same as the
parameters used for the SQL/CLI ``SQLConnect`` function.

The server will be responsible for a particular "cluster of Catalogs" -- which
we may think of as a "database". There's no standard way to pass a database
name with this call, so we can assume that the usual expectation is that
different databases will have different servers. In other words: by specifying
the server, you are indirectly specifying the database that should be opened.

RDADisconnect
.............

**Message Content:**

::

    <nothing>

**What the server is supposed to do:**

Hang up the phone! Cut off the connection that was made with ``RDAConnect``.

The disconnection will probably free the server so it can do other tasks, or
perhaps shut down. The connection could be important for the network too --
you're freeing up a line so that the network server can allow other users to
get on. But TCP/IP is stateless, so the concept of "freeing up a line" is less
meaningful than it would be with other network protocols (such as NETBIOS).

RDAEndTran
..........

**Message Content:**

::

    CompletionType        32-bit INTEGER   flag: COMMIT OR ROLLBACK

**What the server is supposed to:**

The ``RDAEndTran`` marks a transaction boundary, and the flag will usually 
indicate ``COMMIT`` or ``ROLLBACK``, so the usual job is simple: the server 
should end a current transaction with ``COMMIT`` or with ``ROLLBACK``. 

There is a reason that ``RDAEndTran`` is a distinct message -- that makes it 
easier for the network to notice it, without having to know how to parse SQL 
statements. The network might intercept ``RDAEndTran``, because the job of 
"committing" might affect more than just one server job. 

One other flag value that ``CompletionType`` may contain (besides ``COMMIT`` or 
``ROLLBACK``) is: ``PREPARE TO COMMIT``. As part of what we call the "two-phase 
commit" process, the first step is to co-ordinate: get all the servers on the 
network to acknowledge that they are all ready to commit. The second step is 
the ``COMMIT`` itself. Two-phase commit is advanced stuff; many DBMSs will 
refuse to support the ``PREPARE TO COMMIT`` operation. 

RDAClientAttribute
..................

**Message Content:**

::

    ClientAttributes         array           List of attributes

**What the server is supposed to do:**

Take note of what attributes the client has. An "attribute" is an ``env`` or 
``dbc`` or ``stmt`` attribute. That is, it's a number or string that was 
earlier passed to the client, via a ``SQLSetEnvAttr`` or ``SQLSetConnectAttr`` 
or ``SQLSetStmtAttr`` function call. 

The client won't send a new ``RDAClientAttribute`` message every time its own 
attributes change. That would result in too much network traffic. One of the 
features of client/server architecture is: the server doesn't do everything. 
The client is capable of storing data locally for a particular connection and 
only passing on what's necessary when it's necessary. 

RDAStatementPrepare
...................

**Message Content:**

::

    StatementIdent                32-bit integer       sort of a handle
    StatementText                 character string     SQL preparable statement

**What the server is supposed to do:**

Prepare an SQL statement. The client might be able to do some primitive syntax 
checking, but for the full job of binding and parsing, the client has to pass 
the SQL statement to the server. Only the server has direct access to the 
database and its metadata. 

If we were calling ``SQLPrepare``, we'd pass a ``hstmt`` (handle of a 
``stmt``). But a handle is a local identifier. There's no guarantee that a 
handle value will be unique over the whole network. Therefore, instead of a 
``hstmt``, the client must pass a ``StatementIdent``. This is a handle of a 
handle. Given a ``StatementIdent``, the client and server can each look up what 
their respective hstmt values are for the same ``stmt``. 

RDAStatementDeallocate
......................

**Message Content:**

::

    StatementIdent          32-bit integer     sort of a handle

**What the server is supposed to do:**

Free a ``stmt``. Compare the SQL/CLI function 
``SQLFreeHandle(SQL_HANDLE_STMT,...)``.

With client-server, any statement resource (``stmt``) will be duplicated in two
places: the client and the server. When the client is done with a ``stmt``, it
should send an ``RDAStatementDeallocate`` message to the server, so that the
duplicate will be destroyed too.

RDAStatementExecute
...................

**Message Content:**

::

    StatementIdent                32-bit integer       sort of a handle
    ParameterDescriptor           <array>              info re "host variable"
    ParameterData                 <array>              "host variable" content

**What the server is supposed to do:**

Execute an SQL statement. Presumably the statement was prepared earlier, due to 
an ``RDAStatementPrepare`` message with the same ``StatementIdent``. 

The ``ParameterDescriptor`` and ``ParameterData`` fields -- which weren't 
necessary for ``SQLPrepare`` -- represent the solution to a rather tough 
question: what should be done with input parameters? There are no direct RDA 
equivalents for the SQL/CLI functions that handle "parameter descriptors". 
They'd be useless anyway, because SQL/CLI parameter descriptors require 
pointers and pointers have no meaning to a job on a different machine. So what 
happens is: the client bundles up all the input parameter values, and sends 
them as part of the message. 

This might mean that requests get monstrous. But RDA's designers thought it 
would be a bad idea to split ``RDAStatementExecute`` into multiple separate 
messages. What if the messages didn't all arrive in the right order? 

RDAStatementExecDirect
......................

**Message Content:**

::

    StatementIdent                32-bit integer       sort of a handle
    StatementText                 character string     SQL preparable statement
    ParameterDescriptor           <array>              info re "host variable"
    ParameterData                 <array>              "host variable" content

**What the Server is supposed to do:**

Prepare what's in ``StatementText``, then execute it (using the input 
parameters if there are any). 

``RDAStatementExecDirect`` is logically redundant: we could accomplish the same 
thing by sending ``RDAStatementPrepare`` followed by ``RDAStatementExecute``. 
Such redundancy is occasionally justifiable because it's more efficient to send 
one message instead of two. Network traffic is expensive. 

RDAStatementFetchRows
.....................

**Message Content:**

::

    StatementIdent               32-bit integer   sort of a handle
    FetchOrientation             32-bit integer   "next", "first", etc.
    FetchOffset                  32-bit integer   start, relative to last fetch
    FetchCount                   32-bit integer   how many rows to fetch

**What the server is supposed to do:**

Get the values in each of the indicated rows, and ship them to the client. 
Presumably there was an early ``RDAStatementExecute`` or 
``RDAStatementExecDirect`` message for this ``StatementIdent``, which caused a 
query to be executed. So the server has a result set that it can fetch the rows 
from. 

The ``FetchOrientation`` and ``FetchOffset`` parameters contain values 
equivalent to those which are used by the SQL/CLI function ``SQLFetchScroll``. 
For example, ``FetchOrientation`` might equal ``SQL_FETCH_ABSOLUTE`` and 
``FetchOffset`` might equal 55. 

In standard SQL, it's only possible to fetch one row at a time. With RDA -- and 
once again this can be explained by "efficiency" -- it's possible to ask for 
multiple rows to be fetched at once. That's what the ``FetchCount`` parameter 
is for. 

RDAStatementCloseCursor
.......................

**Message Content:**

::

    StatementIdent               32-bit integer   sort of a handle

**What the server is supposed to do:**

Well, close the Cursor. This isn't an end-of-transaction signal, but it does 
tell the server that it can forget about a result set that it created with a 
recent ``SELECT`` statement. 

The client could pass messages in this sequence: *(a)* 
``RDAStatementExecDirect`` with a ``SELECT`` statement so that the server 
creates a result set and Cursor, *(b)* ``RDAStatementFetchRows`` so that the 
server will fetch row values and send them to the client and *(c)* 
``RDAStatementCloseCursor`` so that the server will free (and possibly unlock) 
resources that were allocated for Cursor maintenance. 

RDAStatementCancel
..................

**Message Content:**

::

    StatementIdent               32-bit integer  sort of a handle

**What the server is supposed to do:**

Abort any activity that is taking place for the statement identified by
``StatementIdent``. Since statement execution is atomic, the statement won't be
half-done -- the result is as if the statement was never executed at all.

Why would the client send the statement in the first place, if it didn't want
to finish it? The usual answer is that the client can "change its mind",
perhaps because the execution is taking too long or because some new
information has arrived (such as a Shutdown message from Windows). Or,
consider this scenario:

1. There are two servers. Each server is responsible for a copy of the same 
   database. 

2. The client sends an ``RDAExecDirect`` message to both servers, with the 
   same query. 

3. Inevitably, one of the servers will respond more quickly than the other. 
   Perhaps it's less busy, or perhaps its message packets are just moving by a 
   shorter route. 

4. Once the client receives the response from the fast server, it sends an 
   ``RDAStatementCancel`` message to the slow one, meaning "oh forget it -- I 
   already have the data". 

5. The Server's Response: ``RDAResponse``

**Message Content:**

::

    ServerAttributes            <array>   server's env/dbc/stmt attributes
    Diagnostics                 <array>   errors or warnings
    ParameterDescriptor         <array>   IPD, for RDAStatementPrepare
    RowDescriptor               <array>   metadata, for RDAStatementFetchRows
    Rows                        <array>   data, for RDAStatementFetchRows

The server sends one response message to the client for every request message
that it receives from the client. The contents of responses can vary quite a
bit, but usually you know what sort of responses to expect, by observing what
the original request was. For example, if the request was an
``RDAStatementFetchRows`` message, a reasonable hope is that the response will
contain data from the rows that got fetched.

A single response contains the entire set of results. This means that the
contents of a response are useful for one or many operations that get
performed by the client alone: ``get diagnostics``, ``get attributes`` or ``get
data``. For example, the SQL/CLI function ``SQLGetDiagRec`` does not involve a
network message containing ``RDAGetDiagRec`` -- there is no such thing. Instead,
when an application calls the ``SQLGetDiagRec`` function, the DBMS looks in the
Diagnostics section of the last response that was received from the server.
This means that ``SQLGetDiagRec`` can be called millions of times without
affecting the network or the server. And the same goes for the other ``get``
functions. This also means that the client has to buffer all responses, but
that's okay -- local storage is cheap.

A Short Session
---------------

Let's walk through a short client/server session which involves a single
query. We show client action on the left, server action on the right.

::

    CLIENT                                SERVER

    ... Client is receiving input from    ... Server is idle, just waiting for
    a user via a dialog box               incoming messages

    Client sends RDAConnect message   -->

                                      <-- Server sends response, diagnostic="OK"

    Client sends                      -->
    RDAStatementExecDirect,
    "SELECT * FROM Employees;" message

                                      <-- Server sends response, diagnostic="OK"

    Client sends                      -->
    RDAStatementFetchRows message

                                      <-- Server sends response, diagnostic="OK"
                                          and 2 rows: { ('A',1) ('B',2) }

    Client sends                      -->
    RDAStatementCloseCursor message

                                      <-- Server sends response, diagnostic="OK"

    Client sends                      -->
    RDAEndTran message

                                      <-- Server sends response, diagnostic="OK"

    Client sends                      -->
    RDADisconnect message

                                      <-- Server sends response, diagnostic="OK"

    The network session is over, but      Server is idle again ...
    the client can continue: "FETCH"
    the first row, "FETCH" the second
    row (from local buffers)...

Making it hard
--------------

In our initial tour of RDA, we skipped some non-essential points. We note them
now so that you'll at least be aware of the existence of anything that is
potentially significant.

1. Clients can send multiple requests without waiting for responses. This
   makes for hairy programming, because when responses eventually do arrive, they
   might not be in the right order.

2. There might be multiple clients for one server, which leads to the various
   special considerations that we mentioned in our chapter on concurrency. Or,
   there might be several servers for one client.

3. The network can be heterogeneous, that is, you should be able to connect a
   brand ``X`` client to a brand ``Y`` server. In theory.

4. There is an optional client-side feature: a standard defined CLI (the "RDA
   API"). This is simply a wrapper, so that you can call a function which sends a
   message, without worrying about the details of "how to send a message" over
   TCP/IP.

5. There are optional Schemas which contain Tables which contain information
   about available servers, logs of requests and so on. The Tables can be
   accessed in the same way that Views can be accessed in 
   ``INFORMATION_SCHEMA``.

What good is RDA?
-----------------

In theory, RDA would be a relatively painless way to transfer information via
TCP/IP or other OSI protocols. Programmers could write their own applications
or utilities, such as Intranet servers. But most SQL programmers would prefer
it if RDA was silently included in the DBMS. They want to call ``SQLExecDirect``,
for instance. If the DBMS does the job by silently sending ``RDAExecDirect``
messages to some server, fine.

So all a SQL programmer really needs to know is what you -- we hope! -- have
just gleaned from this discussion of RDA. You  should now be as competent as
you need to be. Specifically:

* You can appreciate database architecture now that you can visualize
  what "clients" and "servers" do.

* You can write better SQL/CLI code since you know what some of the
  underlying effects are.

* You can figure out whether direct use of RDA would help you around
  some specific network problem.

From those examples, it might seem that we're talking about "low-level code"
solutions -- an analogue would be the way that people sometimes write
assembler code snippets in their C programs. We're big fans of that technique
[[ footnote: see our book OPTIMIZING C WITH ASSEMBLY LANGUAGE, R&D Books ]].
But the analogy doesn't really hold: writing for RDA is not inherently more
arcane or low-level than writing any SQL/CLI code. That's clear when you
observe that the parameters are, in almost all cases, the same.
