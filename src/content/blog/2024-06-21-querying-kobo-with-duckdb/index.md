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

``` python
import duckdb

%load_ext sql
conn = duckdb.connect('KoboReader.sqlite')
%sql conn --alias duckdb
%sql SET GLOBAL sqlite_all_varchar = true
```

    The sql extension is already loaded. To reload it, use:
      %reload_ext sql

<span style="None">Running query in &#x27;duckdb&#x27;</span>

<div>

| Success |
|---------|

</div>

``` python
%config SqlMagic.displaylimit = None
```

<span style="None">displaylimit: Value None will be treated as 0 (no limit)</span>

``` python
%%sql
SHOW TABLES;
```

<span style="None">Running query in &#x27;duckdb&#x27;</span>

<div>

| name                  |
|-----------------------|
| AbTest                |
| Achievement           |
| Activity              |
| AnalyticsEvents       |
| Authors               |
| BookAuthors           |
| Bookmark              |
| DbVersion             |
| DropboxItem           |
| Event                 |
| GDriveItem            |
| KoboPlusAssetGroup    |
| KoboPlusAssets        |
| OverDriveCards        |
| OverDriveCheckoutBook |
| OverDriveLibrary      |
| Reviews               |
| Rules                 |
| Shelf                 |
| ShelfContent          |
| SubscriptionProducts  |
| SyncQueue             |
| Tab                   |
| Wishlist              |
| WordList              |
| content               |
| content_keys          |
| content_settings      |
| ratings               |
| shortcover_page       |
| user                  |
| volume_shortcovers    |
| volume_tabs           |

</div>

``` python
%%sql
SELECT COUNT(*) FROM content;
```

<span style="None">Running query in &#x27;duckdb&#x27;</span>

<div>

| count_star() |
|--------------|
| 5026         |

</div>

``` python
%%sql
SELECT * FROM content LIMIT 10
```

<span style="None">Running query in &#x27;duckdb&#x27;</span>

<div>

<table data-quarto-postprocess="true">
<colgroup>
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th data-quarto-table-cell-role="th">ContentID</th>
<th data-quarto-table-cell-role="th">ContentType</th>
<th data-quarto-table-cell-role="th">MimeType</th>
<th data-quarto-table-cell-role="th">BookID</th>
<th data-quarto-table-cell-role="th">BookTitle</th>
<th data-quarto-table-cell-role="th">ImageId</th>
<th data-quarto-table-cell-role="th">Title</th>
<th data-quarto-table-cell-role="th">Attribution</th>
<th data-quarto-table-cell-role="th">Description</th>
<th data-quarto-table-cell-role="th">DateCreated</th>
<th data-quarto-table-cell-role="th">ShortCoverKey</th>
<th data-quarto-table-cell-role="th">adobe_location</th>
<th data-quarto-table-cell-role="th">Publisher</th>
<th data-quarto-table-cell-role="th">IsEncrypted</th>
<th data-quarto-table-cell-role="th">DateLastRead</th>
<th data-quarto-table-cell-role="th">FirstTimeReading</th>
<th data-quarto-table-cell-role="th">ChapterIDBookmarked</th>
<th data-quarto-table-cell-role="th">ParagraphBookmarked</th>
<th data-quarto-table-cell-role="th">BookmarkWordOffset</th>
<th data-quarto-table-cell-role="th">NumShortcovers</th>
<th data-quarto-table-cell-role="th">VolumeIndex</th>
<th data-quarto-table-cell-role="th">___NumPages</th>
<th data-quarto-table-cell-role="th">ReadStatus</th>
<th data-quarto-table-cell-role="th">___SyncTime</th>
<th data-quarto-table-cell-role="th">___UserID</th>
<th data-quarto-table-cell-role="th">PublicationId</th>
<th data-quarto-table-cell-role="th">___FileOffset</th>
<th data-quarto-table-cell-role="th">___FileSize</th>
<th data-quarto-table-cell-role="th">___PercentRead</th>
<th data-quarto-table-cell-role="th">___ExpirationStatus</th>
<th data-quarto-table-cell-role="th">FavouritesIndex</th>
<th data-quarto-table-cell-role="th">Accessibility</th>
<th data-quarto-table-cell-role="th">ContentURL</th>
<th data-quarto-table-cell-role="th">Language</th>
<th data-quarto-table-cell-role="th">BookshelfTags</th>
<th data-quarto-table-cell-role="th">IsDownloaded</th>
<th data-quarto-table-cell-role="th">FeedbackType</th>
<th data-quarto-table-cell-role="th">AverageRating</th>
<th data-quarto-table-cell-role="th">Depth</th>
<th data-quarto-table-cell-role="th">PageProgressDirection</th>
<th data-quarto-table-cell-role="th">InWishlist</th>
<th data-quarto-table-cell-role="th">ISBN</th>
<th data-quarto-table-cell-role="th">WishlistedDate</th>
<th data-quarto-table-cell-role="th">FeedbackTypeSynced</th>
<th data-quarto-table-cell-role="th">IsSocialEnabled</th>
<th data-quarto-table-cell-role="th">EpubType</th>
<th data-quarto-table-cell-role="th">Monetization</th>
<th data-quarto-table-cell-role="th">ExternalId</th>
<th data-quarto-table-cell-role="th">Series</th>
<th data-quarto-table-cell-role="th">SeriesNumber</th>
<th data-quarto-table-cell-role="th">Subtitle</th>
<th data-quarto-table-cell-role="th">WordCount</th>
<th data-quarto-table-cell-role="th">Fallback</th>
<th data-quarto-table-cell-role="th">RestOfBookEstimate</th>
<th data-quarto-table-cell-role="th">CurrentChapterEstimate</th>
<th data-quarto-table-cell-role="th">CurrentChapterProgress</th>
<th data-quarto-table-cell-role="th">PocketStatus</th>
<th data-quarto-table-cell-role="th">UnsyncedPocketChanges</th>
<th data-quarto-table-cell-role="th">ImageUrl</th>
<th data-quarto-table-cell-role="th">DateAdded</th>
<th data-quarto-table-cell-role="th">WorkId</th>
<th data-quarto-table-cell-role="th">Properties</th>
<th data-quarto-table-cell-role="th">RenditionSpread</th>
<th data-quarto-table-cell-role="th">RatingCount</th>
<th data-quarto-table-cell-role="th">ReviewsSyncDate</th>
<th data-quarto-table-cell-role="th">MediaOverlay</th>
<th data-quarto-table-cell-role="th">MediaOverlayType</th>
<th data-quarto-table-cell-role="th">RedirectPreviewUrl</th>
<th data-quarto-table-cell-role="th">PreviewFileSize</th>
<th data-quarto-table-cell-role="th">EntitlementId</th>
<th data-quarto-table-cell-role="th">CrossRevisionId</th>
<th data-quarto-table-cell-role="th">DownloadUrl</th>
<th data-quarto-table-cell-role="th">ReadStateSynced</th>
<th data-quarto-table-cell-role="th">TimesStartedReading</th>
<th data-quarto-table-cell-role="th">TimeSpentReading</th>
<th data-quarto-table-cell-role="th">LastTimeStartedReading</th>
<th data-quarto-table-cell-role="th">LastTimeFinishedReading</th>
<th data-quarto-table-cell-role="th">ApplicableSubscriptions</th>
<th data-quarto-table-cell-role="th">ExternalIds</th>
<th data-quarto-table-cell-role="th">PurchaseRevisionId</th>
<th data-quarto-table-cell-role="th">SeriesID</th>
<th data-quarto-table-cell-role="th">SeriesNumberFloat</th>
<th data-quarto-table-cell-role="th">AdobeLoanExpiration</th>
<th data-quarto-table-cell-role="th">HideFromHomePage</th>
<th data-quarto-table-cell-role="th">IsInternetArchive</th>
<th data-quarto-table-cell-role="th">titleKana</th>
<th data-quarto-table-cell-role="th">subtitleKana</th>
<th data-quarto-table-cell-role="th">seriesKana</th>
<th data-quarto-table-cell-role="th">attributionKana</th>
<th data-quarto-table-cell-role="th">publisherKana</th>
<th data-quarto-table-cell-role="th">IsPurchaseable</th>
<th data-quarto-table-cell-role="th">IsSupported</th>
<th data-quarto-table-cell-role="th">AnnotationsSyncToken</th>
<th data-quarto-table-cell-role="th">DateModified</th>
<th data-quarto-table-cell-role="th">StorePages</th>
<th data-quarto-table-cell-role="th">StoreWordCount</th>
<th data-quarto-table-cell-role="th">StoreTimeToReadLowerEstimate</th>
<th data-quarto-table-cell-role="th">StoreTimeToReadUpperEstimate</th>
<th data-quarto-table-cell-role="th">Duration</th>
<th data-quarto-table-cell-role="th">IsAbridged</th>
<th data-quarto-table-cell-role="th">SyncConflictType</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>43341e67-19ac-43ec-9f51-c92456cd3d9e</td>
<td>6</td>
<td>application/x-kobo-epub+zip</td>
<td>None</td>
<td>None</td>
<td>3a9d5e80-82db-40f6-abbf-6721c945e879</td>
<td>State of Shock (First Family Series, Book 4)</td>
<td>Marie Force</td>
<td><p><em><strong>They never saw this coming…</strong></em></p>
<p>This story picks up right where State of the Union left off with
another wild ride for the First Couple as they navigate work, family and
an all new and extra baffling murder mystery that has Sam pushing the
boundaries to get answers before a killer can strike again. Meanwhile,
Nick contends with the aftermath of his landmark State of the Union
address as a person from his past threatens to undo all the progress
he’s made since a...</p></td>
<td>2022-12-20T05:00:00.0000000Z</td>
<td>None</td>
<td>None</td>
<td>HTJB, Inc.</td>
<td>false</td>
<td>None</td>
<td>true</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>0</td>
<td>2022-12-25T14:46:36Z</td>
<td></td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>None</td>
<td>en</td>
<td>None</td>
<td>false</td>
<td>0</td>
<td>4.733333</td>
<td>0</td>
<td>default</td>
<td>FALSE</td>
<td>9781958035085</td>
<td>None</td>
<td>0</td>
<td>true</td>
<td>13</td>
<td>2</td>
<td>None</td>
<td>First Family Series</td>
<td>4</td>
<td>None</td>
<td>-1</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0.0</td>
<td>0</td>
<td></td>
<td>None</td>
<td>None</td>
<td>b9586df7-fa05-3db2-83f5-e1ecce155e63</td>
<td>None</td>
<td>None</td>
<td>30</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>448797</td>
<td></td>
<td>b9586df7-fa05-3db2-83f5-e1ecce155e63</td>
<td>false</td>
<td>true</td>
<td>0</td>
<td>0</td>
<td>None</td>
<td>None</td>
<td>be9e9ac0-5823-4047-8281-069986c626b9,416bfce4-e4ae-4730-8314-5857dece58a6</td>
<td>od_9092770</td>
<td>None</td>
<td>None</td>
<td>4.0</td>
<td>None</td>
<td>false</td>
<td>false</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>true</td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>false</td>
<td>0</td>
</tr>
<tr class="even">
<td>ca9cc17c-1832-4cd4-b00b-a311780c27b9</td>
<td>6</td>
<td>application/x-kobo-epub+zip</td>
<td>None</td>
<td>None</td>
<td>d94ee9e3-bba4-4a0c-ae21-9e8e0b1b19bc</td>
<td>Queen of Myth and Monsters</td>
<td>Scarlett St. Clair</td>
<td><p><strong>The next book in the vampire fantasy series by <em>USA
Today</em> and international bestselling author Scarlett St.
Clair.</strong></p>
<p>Isolde, newly coronated queen, has finally found a king worthy of her
in the vampire Adrian. But their love for each other has cost Isolde her
father and her homeland. With two opposing goddesses playing mortals and
vampires against one another, Isolde is uncertain who her allies are in
the vampire stronghold of Revekka.</p>
<p>Now, as politics ...</p></td>
<td>2022-12-20T05:00:00.0000000Z</td>
<td>None</td>
<td>None</td>
<td>Sourcebooks</td>
<td>false</td>
<td>None</td>
<td>true</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
<td>-1</td>
<td>0</td>
<td>2022-12-25T14:46:36Z</td>
<td></td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>None</td>
<td>en</td>
<td>None</td>
<td>false</td>
<td>0</td>
<td>4</td>
<td>0</td>
<td>default</td>
<td>FALSE</td>
<td>9781728259666</td>
<td>None</td>
<td>0</td>
<td>true</td>
<td>13</td>
<td>2</td>
<td>None</td>
<td>Adrian X Isolde</td>
<td>2</td>
<td>None</td>
<td>-1</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0.0</td>
<td>0</td>
<td></td>
<td>None</td>
<td>None</td>
<td>c4158de7-8c0d-3d4e-b399-23a2b6b3b256</td>
<td>None</td>
<td>None</td>
<td>2</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>2204122</td>
<td></td>
<td>c4158de7-8c0d-3d4e-b399-23a2b6b3b256</td>
<td>false</td>
<td>true</td>
<td>0</td>
<td>0</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>od_8794546</td>
<td>None</td>
<td>None</td>
<td>2.0</td>
<td>None</td>
<td>false</td>
<td>false</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>true</td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>false</td>
<td>0</td>
</tr>
<tr class="odd">
<td>538ed6aa-e11e-4321-a0a2-97c683e4c47e</td>
<td>6</td>
<td>application/x-kobo-epub+zip</td>
<td>None</td>
<td>None</td>
<td>83114208-491b-4b74-8412-2329646ba692</td>
<td>A Christmas Affair to Remember</td>
<td>Mia Vincy</td>
<td><p><strong>Warm lessons in love on cold winter
nights...</strong></p>
<p>Isaac DeWitt—former sailor, respected investigator, and notorious
flirt—wants a wife, and where better to find one than the winter house
party at Longhope Abbey? But for all his rakish charm, Isaac doesn’t
even know how to kiss a woman, let alone what to do with her in the
marriage bed.</p>
<p>Sylvia Ray—impoverished widow, expert distiller, and safely
betrothed—means to enjoy every minute at the house party before she
s...</p></td>
<td>2022-12-20T05:00:00.0000000Z</td>
<td>None</td>
<td>None</td>
<td>Inner Ballad Press</td>
<td>false</td>
<td>None</td>
<td>true</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>2</td>
<td>-1</td>
<td>0</td>
<td>2022-12-25T14:46:36Z</td>
<td></td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>None</td>
<td>en</td>
<td>None</td>
<td>false</td>
<td>0</td>
<td>4.5</td>
<td>0</td>
<td>default</td>
<td>FALSE</td>
<td>9781925882100</td>
<td>None</td>
<td>0</td>
<td>true</td>
<td>13</td>
<td>2</td>
<td>None</td>
<td>Longhope Abbey</td>
<td>None</td>
<td>None</td>
<td>-1</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0.0</td>
<td>0</td>
<td></td>
<td>None</td>
<td>None</td>
<td>bb165c43-617e-3bf0-9fe7-5d2ba189ed46</td>
<td>None</td>
<td>None</td>
<td>2</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>496334</td>
<td></td>
<td>bb165c43-617e-3bf0-9fe7-5d2ba189ed46</td>
<td>false</td>
<td>true</td>
<td>0</td>
<td>0</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>0.0</td>
<td>None</td>
<td>false</td>
<td>false</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>true</td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>false</td>
<td>0</td>
</tr>
<tr class="even">
<td>22c4c037-71a8-4858-b44c-0af66ef771b2</td>
<td>6</td>
<td>application/x-kobo-epub+zip</td>
<td>None</td>
<td>None</td>
<td>3d95e3ac-1ed8-469d-9b37-6ea24a37071c</td>
<td>Black Sun</td>
<td>Rebecca Roanhorse</td>
<td><p><strong>From the <em>New York Times</em> bestselling author of
<em>Star Wars: Resistance Reborn</em> comes the “engrossing and vibrant”
(Tochi Onyebuchi, author of <em>Riot Baby</em>) first book in the
Between Earth and Sky trilogy inspired by the civilizations of the
Pre-Columbian Americas and woven into a tale of celestial prophecies,
political intrigue, and forbidden magic.</strong></p>
<p>
<em>A god will return</em><br />
<em>When the earth and sky converge</em><br />
&#10;<em>
Under the blac...</td>
<td>2020-10-13T04:00:00.0000000Z</td>
<td>None</td>
<td>None</td>
<td>Gallery / Saga Press</td>
<td>false</td>
<td>None</td>
<td>true</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>0</td>
<td>2022-12-25T23:47:06Z</td>
<td></td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>None</td>
<td>en</td>
<td>None</td>
<td>false</td>
<td>0</td>
<td>4.497326</td>
<td>0</td>
<td>default</td>
<td>FALSE</td>
<td>9781534437692</td>
<td>None</td>
<td>0</td>
<td>true</td>
<td>-1</td>
<td>2</td>
<td>None</td>
<td>Between Earth and Sky</td>
<td>None</td>
<td>None</td>
<td>-1</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0.0</td>
<td>0</td>
<td></td>
<td>None</td>
<td>None</td>
<td>76d31acb-e26a-39bc-a114-b19a49c6b9c3</td>
<td>None</td>
<td>None</td>
<td>187</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>false</td>
<td>0</td>
<td></td>
<td>76d31acb-e26a-39bc-a114-b19a49c6b9c3</td>
<td>false</td>
<td>true</td>
<td>0</td>
<td>0</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>od_5274356</td>
<td>None</td>
<td>None</td>
<td>0.0</td>
<td>None</td>
<td>false</td>
<td>false</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>true</td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>false</td>
<td>0</td>
</tr>
<tr class="odd">
<td>96507f6e-4252-461e-99a4-aae189598376</td>
<td>6</td>
<td>application/x-kobo-epub+zip</td>
<td>None</td>
<td>None</td>
<td>3f975a6b-f4c1-46bf-83fa-189caf6c7fbc</td>
<td>The Bone Shard Daughter</td>
<td>Andrea Stewart</td>
<td><p><strong><em>The Bone Shard Daughter</em> is an unmissable debut
from a major new voice in epic fantasy — a stunning tale of magic,
mystery, and revolution in which the former heir to the emperor will
fight to reclaim her power and her place on the throne.</strong></p>
<p>
<strong>
"One of the best debut fantasy novels of the year." — BuzzFeed
News<br />
"An amazing start to a new trilogy." — Culturess<br />
"It grabs you by the heart and the throat from the first pages and
doesn't let go." —...</td>
<td>2020-09-08T04:00:00.0000000Z</td>
<td>None</td>
<td>None</td>
<td>Orbit</td>
<td>false</td>
<td>None</td>
<td>true</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>0</td>
<td>2022-12-25T23:47:06Z</td>
<td></td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>None</td>
<td>en</td>
<td>None</td>
<td>false</td>
<td>0</td>
<td>4.488095</td>
<td>0</td>
<td>default</td>
<td>FALSE</td>
<td>9780316541442</td>
<td>None</td>
<td>0</td>
<td>true</td>
<td>13</td>
<td>2</td>
<td>None</td>
<td>The Drowning Empire</td>
<td>1</td>
<td>None</td>
<td>-1</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0.0</td>
<td>0</td>
<td></td>
<td>None</td>
<td>None</td>
<td>415b7d7c-ccc1-3909-bc96-c4857fb611ca</td>
<td>None</td>
<td>None</td>
<td>84</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>2136954</td>
<td></td>
<td>75ab574b-c48f-3ddc-ab55-be0ab9a07290</td>
<td>false</td>
<td>true</td>
<td>0</td>
<td>0</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>od_5257087,od_5754534</td>
<td>None</td>
<td>None</td>
<td>1.0</td>
<td>None</td>
<td>false</td>
<td>false</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>true</td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>false</td>
<td>0</td>
</tr>
<tr class="even">
<td>3200b1e2-a3e0-43f4-9c66-92b6dcb333fe</td>
<td>6</td>
<td>application/x-kobo-epub+zip</td>
<td>None</td>
<td>None</td>
<td>db2f7152-4c9a-443a-a5cd-2bff5894065b</td>
<td>The Atlas Six</td>
<td>Olivie Blake</td>
<td><p><strong>An Instant <em>New York Times</em>
Bestseller</strong><br />
<strong>A Vulture Best Fantasy Novel of 2022</strong><br />
<strong>A Goodreads Best Fantasy Choice Award Nominee</strong></p>
<p><strong>The much-acclaimed viral sensation from Olivie
Blake,</strong> <em>The Atlas Six</em>**—**<strong>now newly revised and
edited with additional content.</strong></p>
<p>
<strong>•</strong> <strong>The tag</strong> #theatlassix <strong>has
millions of views on TikTok</strong><br />
<strong...< td></td>
<td>2021-09-28T04:00:00.0000000Z</td>
<td>None</td>
<td>None</td>
<td>Tor Publishing Group</td>
<td>false</td>
<td>None</td>
<td>true</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>0</td>
<td>2022-12-25T23:47:06Z</td>
<td></td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>None</td>
<td>en</td>
<td>None</td>
<td>false</td>
<td>0</td>
<td>3.888199</td>
<td>0</td>
<td>default</td>
<td>FALSE</td>
<td>9781250854551</td>
<td>None</td>
<td>0</td>
<td>true</td>
<td>13</td>
<td>2</td>
<td>None</td>
<td>Atlas Series</td>
<td>1</td>
<td>None</td>
<td>-1</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0.0</td>
<td>0</td>
<td></td>
<td>None</td>
<td>None</td>
<td>1c30d958-71ce-46bd-a84c-6491ce8a0e69</td>
<td>None</td>
<td>None</td>
<td>161</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>1421898</td>
<td></td>
<td>2c56123c-824f-3c9c-a670-af617455590d</td>
<td>false</td>
<td>true</td>
<td>0</td>
<td>0</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>od_7003004,od_7017391</td>
<td>None</td>
<td>None</td>
<td>1.0</td>
<td>None</td>
<td>false</td>
<td>false</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>true</td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>false</td>
<td>0</td>
</tr>
<tr class="odd">
<td>32948a8d-f2dc-4c73-b626-afbeb1d946f7</td>
<td>6</td>
<td>application/x-kobo-epub+zip</td>
<td>None</td>
<td>None</td>
<td>29641cd4-f46a-45ec-a5e1-fa2a6ddff945</td>
<td>The Once and Future Witches</td>
<td>Alix E. Harrow</td>
<td><p><strong>"A gorgeous and thrilling paean to the ferocious power of
women. The characters live, bleed, and roar. "</strong>―Laini Taylor,
<em>New York Times</em> bestselling author</p>
<p><strong>A <em>NEW YORK TIMES</em> BESTSELLER • Winner of the British
Fantasy Award for Best Fantasy Novel • Named One of the Best Books of
the Year by <em>NPR Books</em> • Barnes and Noble •
<em>BookPage</em></strong></p>
<p>
<strong>
In the late 1800s, three sisters use witchcraft to change the course of
his...</td>
<td>2020-10-13T04:00:00.0000000Z</td>
<td>None</td>
<td>None</td>
<td>Orbit</td>
<td>false</td>
<td>None</td>
<td>true</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>0</td>
<td>2022-12-25T23:47:06Z</td>
<td></td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>None</td>
<td>en</td>
<td>None</td>
<td>false</td>
<td>0</td>
<td>4.510067</td>
<td>0</td>
<td>default</td>
<td>FALSE</td>
<td>9780316422031</td>
<td>None</td>
<td>0</td>
<td>true</td>
<td>13</td>
<td>2</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>-1</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0.0</td>
<td>0</td>
<td></td>
<td>None</td>
<td>None</td>
<td>76859f47-268d-3c9f-bcbe-9a4fe3652c5a</td>
<td>None</td>
<td>None</td>
<td>149</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>1621827</td>
<td></td>
<td>a4bec72d-52c3-3796-b6fc-e2f77063de8d</td>
<td>false</td>
<td>true</td>
<td>0</td>
<td>0</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>od_6823480,od_5294818</td>
<td>None</td>
<td>None</td>
<td>0.0</td>
<td>None</td>
<td>false</td>
<td>false</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>true</td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>false</td>
<td>0</td>
</tr>
<tr class="even">
<td>012ded2c-247c-4e19-8733-5139de47927d</td>
<td>6</td>
<td>application/x-kobo-epub+zip</td>
<td>None</td>
<td>None</td>
<td>51ad1843-4f0d-42d9-91d5-86663e93f3e4</td>
<td>The Left-Handed Booksellers of London</td>
<td>Garth Nix</td>
<td><p><strong>A girl’s quest to find her father leads her to an
extended family of magical fighting booksellers who police the mythical
Old World of England when it intrudes on the modern world. From the
bestselling master of teen fantasy, Garth Nix.</strong></p>
<p>In a slightly alternate London in 1983, Susan Arkshaw is looking for
her father, a man she has never met. Crime boss Frank Thringley might be
able to help her, but Susan doesn’t get time to ask Frank any questions
before he is turned...</p></td>
<td>2020-09-22T04:00:00.0000000Z</td>
<td>None</td>
<td>None</td>
<td>HarperCollins</td>
<td>false</td>
<td>None</td>
<td>true</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>0</td>
<td>2022-12-25T23:47:06Z</td>
<td></td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>None</td>
<td>en</td>
<td>None</td>
<td>false</td>
<td>0</td>
<td>4.302631</td>
<td>0</td>
<td>default</td>
<td>FALSE</td>
<td>9780062683274</td>
<td>None</td>
<td>0</td>
<td>true</td>
<td>13</td>
<td>2</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>-1</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0.0</td>
<td>0</td>
<td></td>
<td>None</td>
<td>None</td>
<td>f947d370-c20e-3467-9b17-ed254e0185e0</td>
<td>None</td>
<td>None</td>
<td>76</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>1208221</td>
<td></td>
<td>f947d370-c20e-3467-9b17-ed254e0185e0</td>
<td>false</td>
<td>true</td>
<td>0</td>
<td>0</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>od_5185871</td>
<td>None</td>
<td>None</td>
<td>0.0</td>
<td>None</td>
<td>false</td>
<td>false</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>true</td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>false</td>
<td>0</td>
</tr>
<tr class="odd">
<td>b792542b-ca31-4dd9-8617-6027f0edc9fb</td>
<td>6</td>
<td>application/x-kobo-epub+zip</td>
<td>None</td>
<td>None</td>
<td>53b50910-1a53-416a-995f-f57b874cbeac</td>
<td>A Master of Djinn</td>
<td>P. Djèlí Clark</td>
<td><p>
<strong>Included in NPR’s Favorite Sci-Fi And Fantasy Books Of The Past
Decade (2011-2021)</strong><br />
<strong>A Nebula Award Winner</strong><br />
<strong>A Ignyte Award Winner</strong><br />
<strong>A Compton Crook Award for Best New Novel Winner</strong><br />
<strong>A Locus First Novel Award Winner</strong><br />
<strong>A RUSA Reading List: Fantasy Winner</strong><br />
<strong>A Hugo Award Finalist</strong><br />
<strong>A World Fantasy Award Finalist</strong><br />
&#10;<strong>
A NEI...</td>
<td>2021-05-11T04:00:00.0000000Z</td>
<td>None</td>
<td>None</td>
<td>Tor Publishing Group</td>
<td>false</td>
<td>None</td>
<td>true</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>0</td>
<td>2022-12-25T23:47:06Z</td>
<td></td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>None</td>
<td>en</td>
<td>None</td>
<td>false</td>
<td>0</td>
<td>4.455285</td>
<td>0</td>
<td>default</td>
<td>FALSE</td>
<td>9781250267672</td>
<td>None</td>
<td>0</td>
<td>true</td>
<td>-1</td>
<td>2</td>
<td>None</td>
<td>Dead Djinn Universe</td>
<td>1</td>
<td>None</td>
<td>-1</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0.0</td>
<td>0</td>
<td></td>
<td>None</td>
<td>None</td>
<td>f98aa2ec-c423-46c2-a66e-05ead1ef96ad</td>
<td>None</td>
<td>None</td>
<td>123</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>false</td>
<td>0</td>
<td></td>
<td>d9698ddc-0553-33c3-a249-b92c36ce4720</td>
<td>false</td>
<td>true</td>
<td>0</td>
<td>0</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>od_5716323,od_5716812</td>
<td>None</td>
<td>None</td>
<td>1.0</td>
<td>None</td>
<td>false</td>
<td>false</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>true</td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>false</td>
<td>0</td>
</tr>
<tr class="even">
<td>28a3fec2-1650-4e13-828e-c80290cd5189</td>
<td>6</td>
<td>application/x-kobo-epub+zip</td>
<td>None</td>
<td>None</td>
<td>a7a3160a-5443-4f65-b5e3-f3812bb51eb0</td>
<td>Daughter of the Moon Goddess</td>
<td>Sue Lynn Tan</td>
<td><p><strong>The acclaimed national and international
bestseller</strong></p>
<p><strong>“Epic, romantic, and enthralling from start to
finish.”—Stephanie Garber, #1 <em>New York Times</em> bestselling author
of the Caraval series</strong></p>
<p><strong>“An all-consuming work of literary fantasy that is
breathtaking both for its beauty and its suspense."—<em>BookPage</em>,
starred review</strong></p>
<p>
<strong>
A captivating and romantic debut epic fantasy inspired by the legend of
the Chinese...</td>
<td>2022-01-11T05:00:00.0000000Z</td>
<td>None</td>
<td>None</td>
<td>HarperCollins</td>
<td>false</td>
<td>None</td>
<td>true</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>0</td>
<td>2022-12-25T23:47:06Z</td>
<td></td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>-1</td>
<td>-1</td>
<td>None</td>
<td>en</td>
<td>None</td>
<td>false</td>
<td>0</td>
<td>4.5</td>
<td>0</td>
<td>default</td>
<td>FALSE</td>
<td>9780063031326</td>
<td>None</td>
<td>0</td>
<td>true</td>
<td>13</td>
<td>2</td>
<td>None</td>
<td>Celestial Kingdom</td>
<td>1</td>
<td>A Novel</td>
<td>-1</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0.0</td>
<td>0</td>
<td></td>
<td>None</td>
<td>None</td>
<td>de2d0232-414b-33af-8d20-864aeb78fa43</td>
<td>None</td>
<td>None</td>
<td>108</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>2241953</td>
<td></td>
<td>de2d0232-414b-33af-8d20-864aeb78fa43</td>
<td>false</td>
<td>true</td>
<td>0</td>
<td>0</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>od_6197072</td>
<td>None</td>
<td>None</td>
<td>1.0</td>
<td>None</td>
<td>false</td>
<td>false</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>None</td>
<td>true</td>
<td>true</td>
<td>None</td>
<td>None</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>false</td>
<td>0</td>
</tr>
</tbody>
</table>

</div>
