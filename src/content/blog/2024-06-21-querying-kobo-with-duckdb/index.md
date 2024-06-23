---
title: Using DuckDB to Query Kobo Data
author: Sam Edwardes
date: 2024-06-21
description: hello world
keywords:
- python
- duckdb
- kobo
tags:
- python
---

I have a Kobo eReader that I use for most of my reading. After finishing a recent book, I wanted to review all the highlights and annotations I had made. Kobo provides a built-in way to do this, but the device is rather slow, and the screen is small. This made it challenging to quickly review all my notes.

<!-- TODO: add picture of my kobo -->

After conducting some research, I learned that Kobo uses an on device SQLite database under the hood. Around this time, I was also exploring DuckDB, so I thought this could be an excellent opportunity to delve deeper into DuckDB.

## Locating the SQLite Database

To find the database, you will need to connect your Kobo to your computer. One mounted, you can find the database at `.kobo/KoboReader.sqlite`. On my Mac, the full path is:

```bash
/Volumes/KOBOeReader/.kobo/KoboReader.sqlite
```

## Reading Kobo Data into DuckDB

You can read the sqlite database directly into DuckDB. Use the `-readonly` flag to ensure tha you don't accidentally write to the database.


```bash
duckdb -readonly /Volumes/KOBOeReader/.kobo/KoboReader.sqlite
```

```sql
SHOW TABLES;
```

```
┌───────────────────────┐
│         name          │
│        varchar        │
├───────────────────────┤
│ AbTest                │
│ Achievement           │
│ Activity              │
│ AnalyticsEvents       │
│ Authors               │
│ BookAuthors           │
│ Bookmark              │
│ DbVersion             │
│ DropboxItem           │
│ Event                 │
│ GDriveItem            │
│ KoboPlusAssetGroup    │
│ KoboPlusAssets        │
│ OverDriveCards        │
│ OverDriveCheckoutBook │
│ OverDriveLibrary      │
│ Reviews               │
│ Rules                 │
│ Shelf                 │
│ ShelfContent          │
│ SubscriptionProducts  │
│ SyncQueue             │
│ Tab                   │
│ Wishlist              │
│ WordList              │
│ content               │
│ content_keys          │
│ content_settings      │
│ ratings               │
│ shortcover_page       │
│ user                  │
│ volume_shortcovers    │
│ volume_tabs           │
├───────────────────────┤
│        33 rows        │
└───────────────────────┘
```

I learned from trial and error that the columns do not all have consistent types.

```sql
SELECT * FROM Bookmark LIMIT 3;
```

```
Mismatch Type Error: Invalid type in column "Hidden": column was declared as integer, found "false" of type "text" instead.
```

To get around this change the following sqlite setting:

```sql
SET GLOBAL sqlite_all_varchar = true;
SELECT * FROM Bookmark LIMIT 3;
```

```
┌──────────────────────┬──────────────────────┬───┬──────────────────────┬───────────┐
│      BookmarkID      │       VolumeID       │ … │    ContextString     │   Type    │
│       varchar        │       varchar        │   │       varchar        │  varchar  │
├──────────────────────┼──────────────────────┼───┼──────────────────────┼───────────┤
│ 80b095b7-25f7-4476…  │ 2cbaa292-7eeb-4388…  │ … │ The food trays are…  │ dogear    │
│ 57bf2ec7-1d2a-49df…  │ 27f9517f-0f38-4ea7…  │ … │ I nodded a bit gri…  │ dogear    │
│ ac011d90-1abc-48dd…  │ 866f442e-2078-43c3…  │ … │                      │ highlight │
├──────────────────────┴──────────────────────┴───┴──────────────────────┴───────────┤
│ 3 rows                                                        24 columns (4 shown) │
└────────────────────────────────────────────────────────────────────────────────────┘
```

## DuckDB Basics

There are several functions I found to be the most useful while exploring the data.

- `SHOW TABLES;` - Display all tables in the database.
- `DESCRIBE <table>;` - Display all column names and types
- `.maxrows <n>` - Limit the number of rows displayed.

```sql
SHOW TABLES;
```

```
┌───────────────────────┐
│         name          │
│        varchar        │
├───────────────────────┤
│ AbTest                │
│ Achievement           │
│ Activity              │
│ AnalyticsEvents       │
│ Authors               │
│ BookAuthors           │
│ Bookmark              │
│ DbVersion             │
│ DropboxItem           │
│ Event                 │
│ GDriveItem            │
│ KoboPlusAssetGroup    │
│ KoboPlusAssets        │
│ OverDriveCards        │
│ OverDriveCheckoutBook │
│ OverDriveLibrary      │
│ Reviews               │
│ Rules                 │
│ Shelf                 │
│ ShelfContent          │
│ SubscriptionProducts  │
│ SyncQueue             │
│ Tab                   │
│ Wishlist              │
│ WordList              │
│ content               │
│ content_keys          │
│ content_settings      │
│ ratings               │
│ shortcover_page       │
│ user                  │
│ volume_shortcovers    │
│ volume_tabs           │
├───────────────────────┤
│        33 rows        │
└───────────────────────┘
```


```sql
DESCRIBE Bookmark;
```

```
┌──────────────────────────┬─────────────┬─────────┬─────────┬──────────────────────┬─────────┐
│       column_name        │ column_type │  null   │   key   │       default        │  extra  │
│         varchar          │   varchar   │ varchar │ varchar │       varchar        │ varchar │
├──────────────────────────┼─────────────┼─────────┼─────────┼──────────────────────┼─────────┤
│ BookmarkID               │ VARCHAR     │ NO      │ PRI     │                      │         │
│ VolumeID                 │ VARCHAR     │ NO      │         │                      │         │
│ ContentID                │ VARCHAR     │ NO      │         │                      │         │
│ StartContainerPath       │ VARCHAR     │ NO      │         │                      │         │
│ StartContainerChildIndex │ VARCHAR     │ NO      │         │                      │         │
│ StartOffset              │ VARCHAR     │ NO      │         │                      │         │
│ EndContainerPath         │ VARCHAR     │ NO      │         │                      │         │
│ EndContainerChildIndex   │ VARCHAR     │ NO      │         │                      │         │
│ EndOffset                │ VARCHAR     │ NO      │         │                      │         │
│ Text                     │ VARCHAR     │ YES     │         │                      │         │
│ Annotation               │ VARCHAR     │ YES     │         │                      │         │
│ ExtraAnnotationData      │ VARCHAR     │ YES     │         │                      │         │
│ DateCreated              │ VARCHAR     │ YES     │         │                      │         │
│ ChapterProgress          │ VARCHAR     │ NO      │         │ 0                    │         │
│ Hidden                   │ VARCHAR     │ NO      │         │ 0                    │         │
│ Version                  │ VARCHAR     │ YES     │         │                      │         │
│ DateModified             │ VARCHAR     │ YES     │         │                      │         │
│ Creator                  │ VARCHAR     │ YES     │         │                      │         │
│ UUID                     │ VARCHAR     │ YES     │         │                      │         │
│ UserID                   │ VARCHAR     │ YES     │         │                      │         │
│ SyncTime                 │ VARCHAR     │ YES     │         │                      │         │
│ Published                │ VARCHAR     │ YES     │         │ CAST('f' AS BOOLEAN) │         │
│ ContextString            │ VARCHAR     │ YES     │         │                      │         │
│ Type                     │ VARCHAR     │ YES     │         │                      │         │
├──────────────────────────┴─────────────┴─────────┴─────────┴──────────────────────┴─────────┤
│ 24 rows                                                                           6 columns │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

```sql
.maxrows 3
SELECT * FROM Bookmark;
```

```
┌──────────────────────┬──────────────────────┬──────────────────────┬──────────────────────┬───┬──────────────────────┬───────────┬──────────────────────┬───────────┐
│      BookmarkID      │       VolumeID       │      ContentID       │  StartContainerPath  │ … │       SyncTime       │ Published │    ContextString     │   Type    │
│       varchar        │       varchar        │       varchar        │       varchar        │   │       varchar        │  varchar  │       varchar        │  varchar  │
├──────────────────────┼──────────────────────┼──────────────────────┼──────────────────────┼───┼──────────────────────┼───────────┼──────────────────────┼───────────┤
│ 80b095b7-25f7-4476…  │ 2cbaa292-7eeb-4388…  │ 2cbaa292-7eeb-4388…  │ OEBPS/xhtml/Novi_9…  │ … │ 2022-12-30T15:24:41Z │ false     │ The food trays are…  │ dogear    │
│ 57bf2ec7-1d2a-49df…  │ 27f9517f-0f38-4ea7…  │ OEBPS/xhtml/Novi_9…  │ OEBPS/xhtml/Novi_9…  │ … │ 2023-03-07T06:17:47Z │ false     │ I nodded a bit gri…  │ dogear    │
│          ·           │          ·           │          ·           │          ·           │ · │          ·           │   ·       │          ·           │   ·       │
│          ·           │          ·           │          ·           │          ·           │ · │          ·           │   ·       │          ·           │   ·       │
│          ·           │          ·           │          ·           │          ·           │ · │          ·           │   ·       │          ·           │   ·       │
│ c18c2ca2-393b-4eda…  │ file:///mnt/onboar…  │ file:///mnt/onboar…  │ OEBPS/Text/chapter…  │ … │                      │ false     │                      │ highlight │
├──────────────────────┴──────────────────────┴──────────────────────┴──────────────────────┴───┴──────────────────────┴───────────┴──────────────────────┴───────────┤
│ 31 rows (3 shown)                                                                                                                              24 columns (8 shown) │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

```sql
.maxrows 10
SELECT * FROM Bookmark;
```

```
┌──────────────────────┬──────────────────────┬──────────────────────┬──────────────────────┬───┬──────────────────────┬───────────┬──────────────────────┬───────────┐
│      BookmarkID      │       VolumeID       │      ContentID       │  StartContainerPath  │ … │       SyncTime       │ Published │    ContextString     │   Type    │
│       varchar        │       varchar        │       varchar        │       varchar        │   │       varchar        │  varchar  │       varchar        │  varchar  │
├──────────────────────┼──────────────────────┼──────────────────────┼──────────────────────┼───┼──────────────────────┼───────────┼──────────────────────┼───────────┤
│ 80b095b7-25f7-4476…  │ 2cbaa292-7eeb-4388…  │ 2cbaa292-7eeb-4388…  │ OEBPS/xhtml/Novi_9…  │ … │ 2022-12-30T15:24:41Z │ false     │ The food trays are…  │ dogear    │
│ 57bf2ec7-1d2a-49df…  │ 27f9517f-0f38-4ea7…  │ OEBPS/xhtml/Novi_9…  │ OEBPS/xhtml/Novi_9…  │ … │ 2023-03-07T06:17:47Z │ false     │ I nodded a bit gri…  │ dogear    │
│ ac011d90-1abc-48dd…  │ 866f442e-2078-43c3…  │ OEBPS/xhtml/Bogd_9…  │ span#kobo\.114\.3    │ … │ 2023-08-16T11:57:56Z │ false     │                      │ highlight │
│ 0869a5e2-fa89-4f3b…  │ 866f442e-2078-43c3…  │ OEBPS/xhtml/Bogd_9…  │ span#kobo\.115\.1    │ … │ 2023-08-16T11:57:56Z │ false     │                      │ highlight │
│ 08305a0f-2142-4b8d…  │ 866f442e-2078-43c3…  │ OEBPS/xhtml/Bogd_9…  │ span#kobo\.174\.2    │ … │ 2023-08-16T11:57:56Z │ false     │                      │ highlight │
│          ·           │          ·           │          ·           │         ·            │ · │          ·           │   ·       │          ·           │     ·     │
│          ·           │          ·           │          ·           │         ·            │ · │          ·           │   ·       │          ·           │     ·     │
│          ·           │          ·           │          ·           │         ·            │ · │          ·           │   ·       │          ·           │     ·     │
│ 4900a30a-8f81-499a…  │ file:///mnt/onboar…  │ file:///mnt/onboar…  │ OEBPS/Text/introdu…  │ … │                      │ false     │                      │ highlight │
│ c8ecdc87-a1dd-4a36…  │ file:///mnt/onboar…  │ file:///mnt/onboar…  │ OEBPS/Text/introdu…  │ … │                      │ false     │                      │ highlight │
│ 6c146f08-b82b-4991…  │ file:///mnt/onboar…  │ file:///mnt/onboar…  │ OEBPS/Text/introdu…  │ … │                      │ false     │                      │ highlight │
│ 638d7b45-217d-4866…  │ file:///mnt/onboar…  │ file:///mnt/onboar…  │ OEBPS/Text/chapter…  │ … │                      │ false     │                      │ highlight │
│ c18c2ca2-393b-4eda…  │ file:///mnt/onboar…  │ file:///mnt/onboar…  │ OEBPS/Text/chapter…  │ … │                      │ false     │                      │ highlight │
├──────────────────────┴──────────────────────┴──────────────────────┴──────────────────────┴───┴──────────────────────┴───────────┴──────────────────────┴───────────┤
│ 31 rows (10 shown)                                                                                                                             24 columns (8 shown) │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Understanding your library

I found the following tables to have the most interesting and relevant data.

- `content` - Has 1 row for each chapter in each book.
- `Bookmark` - Has 1 row for each highlight/annotation.

The database has a total of 33 tables, but I did not find very much useful data in the other tables.

## Query: List all books

```sql
.maxrows 5
SELECT DISTINCT BookTitle FROM content
WHERE BookTitle IS NOT NULL
ORDER BY BookTitle;
```

```
┌─────────────────────────────────────┐
│              BookTitle              │
│               varchar               │
├─────────────────────────────────────┤
│ 2034: A Novel of the Next World War │
│ A Deadly Education                  │
│ A Half-Built Garden                 │
│          ·                          │
│          ·                          │
│          ·                          │
│ When McKinsey Comes to Town         │
│ White Fragility                     │
├─────────────────────────────────────┤
│          60 rows (5 shown)          │
└─────────────────────────────────────┘
```

## Query: List all books and chapters

```sql
.maxrows 10
SELECT
    BookTitle,
    Title,
    CAST (VolumeIndex AS INT) AS VolumeIndex
FROM content
WHERE
    BookTitle IS NOT NULL
    AND MimeType != 'application/xhtml+xml'
ORDER BY BookTitle, VolumeIndex;
```

```
┌─────────────────────────────────────┬─────────────────────────────────────────────────────┬─────────────┐
│              BookTitle              │                        Title                        │ VolumeIndex │
│               varchar               │                       varchar                       │    int32    │
├─────────────────────────────────────┼─────────────────────────────────────────────────────┼─────────────┤
│ 2034: A Novel of the Next World War │ Cover                                               │           0 │
│ 2034: A Novel of the Next World War │ Also by Elliot Ackerman and Admiral James Stavridis │           1 │
│ 2034: A Novel of the Next World War │ Title Page                                          │           2 │
│ 2034: A Novel of the Next World War │ Copyright                                           │           3 │
│ 2034: A Novel of the Next World War │ Epigraph                                            │           4 │
│        ·                            │    ·                                                │           · │
│        ·                            │    ·                                                │           · │
│        ·                            │    ·                                                │           · │
│ White Fragility                     │ 12. Where Do We Go from Here?                       │          18 │
│ White Fragility                     │ Resources for Continuing Education                  │          19 │
│ White Fragility                     │ Acknowledgments                                     │          20 │
│ White Fragility                     │ Notes                                               │          21 │
│ White Fragility                     │ Copyright                                           │          22 │
├─────────────────────────────────────┴─────────────────────────────────────────────────────┴─────────────┤
│ 2585 rows (10 shown)                                                                          3 columns │
└─────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Query: List all highlights and annotations

All of your text highlights can be found in `Bookmark.Text`. If you left a note within that highlight, it can be found in `Bookmark.Annotation`. Using a join, you can enrich the Bookmark table with info about the book and chapter.

```sql
.maxrows 10
SELECT
    c.BookTitle,
    c.Title AS ChapterTitle,
    b.DateCreated,
    b.Text,
    b.Annotation,
    b.Type,
    b.ChapterProgress
FROM Bookmark AS b
LEFT JOIN content AS c on b.ContentID = c.ContentID
WHERE b.Type = 'highlight' OR b.Type ='note'
ORDER BY c.BookTitle, b.ChapterProgress;
```

```
┌──────────────────────┬──────────────────────┬──────────────────────┬─────────────────────────────────────────────────────────────┬────────────┬───────────┬────────────────────┐
│      BookTitle       │     ChapterTitle     │     DateCreated      │                            Text                             │ Annotation │   Type    │  ChapterProgress   │
│       varchar        │       varchar        │       varchar        │                           varchar                           │  varchar   │  varchar  │      varchar       │
├──────────────────────┼──────────────────────┼──────────────────────┼─────────────────────────────────────────────────────────────┼────────────┼───────────┼────────────────────┤
│ Artificial Condition │ Chapter Seven        │ 2023-12-27T13:14:0…  │ In the creche, our moms always said that fear was an arti…  │            │ highlight │ 0.712765957446809  │
│ INSPIRED: How to C…  │ Key Responsibilities │ 2024-04-04T05:38:2…  │ \n At one level, the responsibilities of the product mana…  │            │ highlight │ 0.180602           │
│ INSPIRED: How to C…  │ Deep Knowledge of …  │ 2024-04-04T05:38:5…  │ To summarize, these are the four critical contributions y…  │            │ highlight │ 0.190635           │
│ INSPIRED: How to C…  │ CHAPTER 33: Princi…  │ 2024-04-04T05:40:4…  │ The purpose of product discovery is to address these crit…  │            │ highlight │ 0.511706           │
│ INSPIRED: How to C…  │ CHAPTER 35: Opport…  │ 2024-04-04T05:42:2…  │ An opportunity assessment is an extremely simple techniqu…  │            │ highlight │ 0.551839           │
│          ·           │          ·           │          ·           │                              ·                              │     ·      │     ·     │    ·               │
│          ·           │          ·           │          ·           │                              ·                              │     ·      │     ·     │    ·               │
│          ·           │          ·           │          ·           │                              ·                              │     ·      │     ·     │    ·               │
│ Some People Need K…  │ Chapter 2: The Sur…  │ 2024-01-02T06:22:4…  │ Four months later, President McKinley demanded that Filip…  │            │ highlight │ 0.0704607046070461 │
│ There Must Be a Po…  │ Epilogue             │ 2024-05-20T15:25:2…  │ . As a generator of instant wealth, the Net may now be a …  │            │ highlight │ 0.933333333333333  │
│                      │                      │ 2023-07-20T05:59:4…  │ Cesar                                                       │            │ highlight │ 0.517241379310345  │
│                      │                      │ 2023-07-20T05:59:5…  │ —\n\t\t\tSome ICE staffers were growing frustrated with     │            │ highlight │ 0.517241379310345  │
│                      │                      │ 2023-08-06T07:52:0…  │ looking for is how much we can see, how we would log things │            │ highlight │ 0.806451612903226  │
├──────────────────────┴──────────────────────┴──────────────────────┴─────────────────────────────────────────────────────────────┴────────────┴───────────┴────────────────────┤
│ 29 rows (10 shown)                                                                                                                                                   7 columns │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Exporting Data

DuckDB simplifies exporting data into various formats. After determining the appropriate query to find all highlights and annotations for the completed book, I exported the information to a CSV file. This allowed me to easily copy and paste the table into Notion for further review and note-taking.

```sql
COPY (
    SELECT
        c.BookTitle,
        c.Title AS ChapterTitle,
        b.DateCreated,
        b.Text,
        b.Annotation,
        b.Type,
        b.ChapterProgress
    FROM Bookmark AS b
    LEFT JOIN content AS c on b.ContentID = c.ContentID
    WHERE b.Type = 'highlight' OR b.Type ='note'
    ORDER BY c.BookTitle, b.ChapterProgress
) TO 'highlights.csv' (HEADER, DELIMITER ',');
```