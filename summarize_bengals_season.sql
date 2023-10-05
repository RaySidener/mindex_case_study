select sum(yards_chase) as chase_total_yards,
  sum(yards_boyd) as boyd_total_yards,
  sum(yards_higgins) as higgins_total_yards,
  concat(
	sum(case when result = 'Win' then 1 end), 
	'-', 
	sum(case when result = 'Loss' then 1 end)) as win_lose_ratio
from postgres.public.ray_sidener;
