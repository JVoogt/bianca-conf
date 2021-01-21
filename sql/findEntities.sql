WITH CTE
AS
(
SELECT domain, entity_id, max(created) mc, max(last_changed) lc, max(last_updated) lu
FROM states
GROUP BY domain, entity_id
)
SELECT  *
FROM    CTE
WHERE   domain = 'device_tracker'
-- WHERE   mc < date('now','-1 day');