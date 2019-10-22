.. highlight:: text

=======
Preface
=======

If you've ever used a relational database product, chances are that you're
already familiar with SQL -- the internationally-accepted, standard programming
language for databases whic is supported by the vast majority of relational
database management system (DBMS) products available today. You may also have
noticed that, despite the large number of "reference" works that claim to
describe standard SQL, not a single one provides a complete, accurate and
example-filled description of the entire SQL Standard. This book was written to
fill that void.

.. rubric:: Table of Contents

.. contents::
       :local:

Who Should Read this Book?
==========================

This book will be valuable to anyone who works with a DBMS that supports SQL.
While our emphasis is on programming with SQL, you do not need to be a
programmer to learn SQL from our examples. We do assume you know something
about Windows and something about C, but our main concern is that you are
interested in using "ANSI Standard SQL" in your projects. This is both a
beginner's and an advanced-user's book. Our hope is that a beginner will be
able to avoid the traditional "for beginners" books which, sadly, contain so
much drivel that it is impossible to advance from them without re-learning
everything.

Your Windows knowledge needn't be extensive, as we won't be getting into the
details of the Windows Application Programming Interface (API). We'll touch
only on things that occur in all versions of Windows, and occasionally
analogize with Windows concepts and terms.

As for C, we assume you can read simple C programs, even if your favourite
programming language is something else. We want to show you examples of SQL as
it's used in programming projects -- that is, in company with a "host language"
-- and C seemed the convenient choice. All example programs shown provided are
short.

What's In It?
=============

World's Longest SQL Poem (for obvious reasons)
----------------------------------------------

   ::

       All the snake-oil peddlers say, there's a fast and easy way,
       To get your SQL program up and running,
       But they're silent re the traps, that cause subtly buggy apps,
       For to catch the unaware a chasm's yawning!

       Date-arithmetic exceptions, auto-rollbacked disconnections,
       Bit precisions, overflows, collate coercions,
       And how NULL affects your summing, for to keep your DB humming,
       You must know what happens in all vendors' versions!

       Should this field be DOUBLE PRECISION?
       Will logic rules soon see revision?
       By the ANSI:Databases sub-committee?
       When you DROP should you CASCADE?
       How are NATURAL joins made?
       Re UNIQUE-keys matching check the nitty-gritty!

       Yeah the true and standard facts, you'll avoid those later hacks
       That make Structured Query Language such a bore,
       You'll find tips and charts aplenty, in this one-thousand-and-twenty
       Four page volume (with an index), and yet more!

   -- Author anon (also for obvious reasons)

This book describes the SQL syntax a DBMS must support to comply with the
International Organization for Standardization (ISO) document ISO/IEC
9075:1999 Database Language SQL, also adopted as the American National
Standards Institute (ANSI) document X3.135-1999 Database Language SQL --
familiarly known as SQL3, standard SQL or ANSI SQL. We will use the more
familiar terms "SQL" or "SQL3" to describe Standard-conforming SQL in this book,
rather than the formal term SQL-99.

It's true that some features discussed in this book aren't in <fill in your
DBMS name here>. That's no reason to ignore them, because sooner or later they
will be there, due to pressure on serious vendors to adhere to the SQL
Standard.

Why Read It?
------------

You need to know SQL so you've been looking for an accurate reference work
that describes the entire SQL Standard by way of examples. This is that book.

How much of what you need to know is in this book? Well, it's impossible for a
single book to contain everything you need. We guarantee that the coverage is
complete for the SQL language itself, and is adequate for subjects that
closely relate to SQL. Let's express "what you will know" as a percentage of
"what you should know", with an assumption that you're an average person:

::

   ## SQL3 Standard "foundation"           90%
   ## Earlier ANSI and ISO Standards      100%
   ## SQL/CLI                             100%
   ## Embedded SQL and host languages      40%
   ## Object orientation (UDTs)            20%
   ## Relational database theory           10%
   ## Design                               10%
   ## Quirks of specific vendors' dialects  5%

"Complete" does not mean that everything which could be said about SQL
will be said here. SQL is big. More exactly, it means that we will
never refer you to further published material saying "the details are in the
official standard document" or "further discussion is outside the scope of
this book".

Further Information
-------------------

When you look at our Table of Contents, you'll see that this book
includes several Appendices, but only on the accompanying CD-ROM,
to keep the book from becoming too unwieldy. Of the Appendix files,
we especially recommend Appendix F, the Glossary. It provides
definitions for all the SQL technical terms we use.
