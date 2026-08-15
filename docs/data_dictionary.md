# Data Dictionary — ESA DISCOS Launch Failures

## טבלת האירועים הראשונית

קובץ: `data/processed/esa_discos_failed_launches_since_2000.csv`

| שדה | משמעות |
| --- | --- |
| `launch_id` | מזהה פנימי של רשומת השיגור ב־DISCOS |
| `epoch` | תאריך ושעת השיגור, UTC |
| `flight_no` | מספר הטיסה של כלי השיגור כפי שמופיע ב־DISCOS |
| `cospar_launch_no` | מספר השיגור בפורמט COSPAR |
| `failure` | דגל כשל בוליאני; כל הרשומות בקובץ הן `true` |
| `vehicle_ids` / `vehicle_names` | מזהה ושם כלי השיגור המקושר |
| `site_ids` / `site_names` | מזהה ושם אתר השיגור המקושר |
| `entity_ids` / `entity_names` | מדינות או ארגונים המקושרים לשיגור, אם הוחזרו |
| `object_ids` / `object_names` | אובייקטים מקושרים, אם הוחזרו |

ערכים מרובים מופרדים ב־` | `. ערך ריק פירושו שה־API לא החזיר קשר עבור אותו אירוע; אין להסיק מכך בהכרח שהישות אינה קיימת בעולם האמיתי.

## כיסוי הקריאה

הקריאה נעשתה עם `filter=eq(failure,true)`, `sort=-epoch`, `include=vehicle,site,entities,objects` ועמודים 1–2 בגודל 100. סינון התאריך `epoch >= 2000-01-01` יושם לאחר ההורדה, מפני שבדיקת התחביר הראשונית של סינון תאריך בצד ה־API נדחתה.

| מדד | תוצאה |
| --- | --- |
| אירועי כשל מאז 2000 | 119 |
| קשר vehicle | 119 מתוך 119 |
| קשר site | 119 מתוך 119 |
| קשר entities לא ריק | 44 מתוך 119 |
| קשר objects לא ריק | 0 מתוך 119 |

## שדות זמינים בקבצי ה־JSON

`launch`: `epoch`, `flightNo`, `cosparLaunchNo`, `failure`.

`vehicle`: `name`, `mass`, `thrustLevel`, מידות, `numStages`, קיבולות LEO/SSO/GTO/GEO/escape, ומספר השיגורים המוצלחים והכושלים.

`launchSite`: `name`, `pads`, `azimuths`, `constraints`, קווי רוחב/אורך וגובה.

`organisation`: `name`, `dateRange`; `country`: `name`.

## כללי הרחבה

- לא משנים את קבצי `data/raw/` לאחר שמירה.
- כל העשרה או תיקון נשמרים בטבלאה חדשה תחת `data/processed/` יחד עם תיעוד מקור ושיטת התאמה.
- טוקנים, מפתחות API וסודות אינם נשמרים במאגר.
