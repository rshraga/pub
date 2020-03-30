condition_query = """
select dsysrtky,sum(dx1) as dx1,sum(dx2) as dx2, sum(dx3) as dx3, sum(dx4) as dx4, sum(dx5) as dx5, sum(dx6) as dx6,
sum(dx7) as dx7, sum(dx8) as dx8, sum(dx9) as dx9, sum(dx10) as dx10, sum(dx11) as dx11, sum(dx12) as dx12, sum(dx13) as dx13,
sum(dx14) as dx14, sum(dx15) as dx15, sum(dx16) as dx16, sum(dx17) as dx17, sum(dx18) as dx18, sum(dx19) as dx19, sum(dx20) as dx20,
sum(dx21) as dx21, sum(dx22) as dx22, sum(dx23) as dx23, sum(dx24) as dx24, sum(dx25) as dx25, sum(dx26) as dx26,
max(dx_score) as dx_max,
avg(dx_score) as dx_avg,
stddev_samp(dx_score) as dx_std
from
(select s.dsysrtky, c.dx1::int as dx1, c.dx2::int as dx2, c.dx3::int as dx3, c.dx4::int as dx4, c.dx5::int as dx5, c.dx6::int as dx6,
c.dx7::int as dx7, c.dx8::int as dx8, c.dx9::int as dx9, c.dx10::int as dx10, c.dx11::int as dx11, c.dx12::int as dx12, c.dx13::int as dx13,
c.dx14::int as dx14, c.dx15::int as dx15, c.dx16::int as dx16, c.dx17::int as dx17, c.dx18::int as dx18, c.dx19::int as dx19, c.dx20::int as dx20,
c.dx21::int as dx21, c.dx22::int as dx22, c.dx23::int as dx23, c.dx24::int as dx24, c.dx25::int as dx25, c.dx26::int as dx26,
dx2::int + dx20::int + dx11::int + 2*dx13::int + 2*dx9::int + 2*dx8::int + 2*dx21::int + 3*dx3::int + 3*dx19::int as dx_score
from copd_2016 s 
inner join car_claimsk c
on s.dsysrtky = c.dsysrtky
where {cond}
UNION
select s.dsysrtky, c.dx1::int as dx1, c.dx2::int as dx2, c.dx3::int as dx3, c.dx4::int as dx4, c.dx5::int as dx5, c.dx6::int as dx6,
c.dx7::int as dx7, c.dx8::int as dx8, c.dx9::int as dx9, c.dx10::int as dx10, c.dx11::int as dx11, c.dx12::int as dx12, c.dx13::int as dx13,
c.dx14::int as dx14, c.dx15::int as dx15, c.dx16::int as dx16, c.dx17::int as dx17, c.dx18::int as dx18, c.dx19::int as dx19, c.dx20::int as dx20,
c.dx21::int as dx21, c.dx22::int as dx22, c.dx23::int as dx23, c.dx24::int as dx24, c.dx25::int as dx25, c.dx26::int as dx26,
dx2::int + dx20::int + dx11::int + 2*dx13::int + 2*dx9::int + 2*dx8::int + 2*dx21::int + 3*dx3::int + 3*dx19::int as dx_score
from copd_2016 s 
inner join out_claimsk c
on s.dsysrtky = c.dsysrtky
 where {cond}
UNION
select s.dsysrtky, c.dx1::int as dx1, c.dx2::int as dx2, c.dx3::int as dx3, c.dx4::int as dx4, c.dx5::int as dx5, c.dx6::int as dx6,
c.dx7::int as dx7, c.dx8::int as dx8, c.dx9::int as dx9, c.dx10::int as dx10, c.dx11::int as dx11, c.dx12::int as dx12, c.dx13::int as dx13,
c.dx14::int as dx14, c.dx15::int as dx15, c.dx16::int as dx16, c.dx17::int as dx17, c.dx18::int as dx18, c.dx19::int as dx19, c.dx20::int as dx20,
c.dx21::int as dx21, c.dx22::int as dx22, c.dx23::int as dx23, c.dx24::int as dx24, c.dx25::int as dx25, c.dx26::int as dx26,
dx2::int + dx20::int + dx11::int + 2*dx13::int + 2*dx9::int + 2*dx8::int + 2*dx21::int + 3*dx3::int + 3*dx19::int as dx_score
from copd_2016 s 
inner join hha_claimsk c
on s.dsysrtky = c.dsysrtky
 where {cond}
UNION
select s.dsysrtky, c.dx1::int as dx1, c.dx2::int as dx2, c.dx3::int as dx3, c.dx4::int as dx4, c.dx5::int as dx5, c.dx6::int as dx6,
c.dx7::int as dx7, c.dx8::int as dx8, c.dx9::int as dx9, c.dx10::int as dx10, c.dx11::int as dx11, c.dx12::int as dx12, c.dx13::int as dx13,
c.dx14::int as dx14, c.dx15::int as dx15, c.dx16::int as dx16, c.dx17::int as dx17, c.dx18::int as dx18, c.dx19::int as dx19, c.dx20::int as dx20,
c.dx21::int as dx21, c.dx22::int as dx22, c.dx23::int as dx23, c.dx24::int as dx24, c.dx25::int as dx25, c.dx26::int as dx26,
dx2::int + dx20::int + dx11::int + 2*dx13::int + 2*dx9::int + 2*dx8::int + 2*dx21::int + 3*dx3::int + 3*dx19::int as dx_score
from copd_2016 s 
inner join snf_claimsk c
on s.dsysrtky = c.dsysrtky
 where {cond}
UNION
select s.dsysrtky, c.dx1::int as dx1, c.dx2::int as dx2, c.dx3::int as dx3, c.dx4::int as dx4, c.dx5::int as dx5, c.dx6::int as dx6,
c.dx7::int as dx7, c.dx8::int as dx8, c.dx9::int as dx9, c.dx10::int as dx10, c.dx11::int as dx11, c.dx12::int as dx12, c.dx13::int as dx13,
c.dx14::int as dx14, c.dx15::int as dx15, c.dx16::int as dx16, c.dx17::int as dx17, c.dx18::int as dx18, c.dx19::int as dx19, c.dx20::int as dx20,
c.dx21::int as dx21, c.dx22::int as dx22, c.dx23::int as dx23, c.dx24::int as dx24, c.dx25::int as dx25, c.dx26::int as dx26,
dx2::int + dx20::int + dx11::int + 2*dx13::int + 2*dx9::int + 2*dx8::int + 2*dx21::int + 3*dx3::int + 3*dx19::int as dx_score
from copd_2016 s 
inner join inp_claimsk c
on s.dsysrtky = c.dsysrtky
 where {cond}
)subq
group by dsysrtky;"""

dme_query = """
select s.dsysrtky, 
CASE WHEN sum(c.dx1::int)  > 0 then 1 else 0 end as dme_dx1, 
CASE WHEN sum(c.dx2::int) > 0 then 1 else 0 end as dme_dx2, 
CASE WHEN sum(c.dx3::int) > 0 then 1 else 0 end as dme_dx3
from copd_2016 s 
left join dme_linek c
on s.dsysrtky = c.dsysrtky
where {cond}
group by s.dsysrtky;"""

ip_query = """
select s.dsysrtky, 
count(distinct ADMSN_DT) as ip_dist,
sum(util_day) as ip_tot,
max(util_day) as ip_max,
count(distinct case when drg_cd in ('202','203','207','208','204','190','191','192','189','177','178','179') then admsn_dt else null end) as ip_copd_dist,
sum(case when drg_cd in ('202','203','207','208','204','190','191','192','189','177','178','179') then util_day else 0 end) as ip_copd_tot,
count(distinct case when stus_cd='01' then ADMSN_DT else null end) as ip_home,
'2016-12-31'- max(thru_dt) as ip_days_since
from copd_2016 s 
left join inp_claimsk c
on s.dsysrtky = c.dsysrtky
where {cond}
and TYPE_ADM in ('1','2')
group by s.dsysrtky;"""

hha_query = """
select s.dsysrtky, 
sum(visitcnt) as hha_tot,
sum(case when dx9 = '1' then visitcnt else 0 end) as hha_copd_tot
from copd_2016 s 
left join hha_claimsk c
on s.dsysrtky = c.dsysrtky
where {cond}
group by s.dsysrtky;
"""

snf_query = """
select s.dsysrtky, 
sum(UTIL_DAY) as snf_tot,
max(UTIL_DAY) as snf_max,
count(distinct admsn_dt) as snf_dist
from copd_2016 s 
inner join snf_claimsk c
on s.dsysrtky = c.dsysrtky
	where {cond}
group by s.dsysrtky;"""


er_query = """
select dsysrtky,
sum(er_visits) as er_tot, 
min(er_days_since) as er_days_since
from
(
select s.dsysrtky, 
count(distinct thru_dt) as er_visits,
	'2016-12-31' - max(thru_dt) as er_days_since
from copd_2016 s 
inner join out_revenuek c
on s.dsysrtky = c.dsysrtky
	where {cond}
	and rev_cntr in ('0450','0451','0452','0453','0454','0455','0456','0457','0458','0459', '0981')
group by s.dsysrtky
union 
select s.dsysrtky, 
count(distinct thru_dt) as er_visits,
	'2016-12-31' - max(thru_dt) as er_days_since
from copd_2016 s 
inner join inp_revenuek c
on s.dsysrtky = c.dsysrtky
	where {cond}
	and rev_cntr in ('0450','0451','0452','0453','0454','0455','0456','0457','0458','0459', '0981')
group by s.dsysrtky
)subq
group by dsysrtky;
"""


prov_query = """
select 
dsysrtky,
count(distinct case when prov = '30' then thru_dt else null end) as _30_cnt,
count(distinct case when prov = '69' then thru_dt else null end) as _69_cnt,
count(distinct case when prov = '06' then thru_dt else null end) as card_cnt,
count(distinct case when prov = '93' then thru_dt else null end) as _93_cnt,
count(distinct case when prov = '50' then thru_dt else null end) as _50_cnt,
count(distinct case when prov = '18' then thru_dt else null end) as _18_cnt,
count(distinct case when prov = '97' then thru_dt else null end) as _97_cnt,
count(distinct case when prov = '29' then thru_dt else null end) as pulm_cnt,
count(distinct case when prov = '22' then thru_dt else null end) as _22_cnt,
count(distinct case when prov = '05' then thru_dt else null end) as _05_cnt,
count(distinct case when prov = '07' then thru_dt else null end) as _07_cnt,
count(distinct case when prov = '48' then thru_dt else null end) as _48_cnt,
count(distinct case when prov = '41' then thru_dt else null end) as _41_cnt,
count(distinct case when prov = '20' then thru_dt else null end) as _20_cnt,
count(distinct case when prov = '43' then thru_dt else null end) as _43_cnt,
count(distinct case when prov = '59' then thru_dt else null end) as _59_cnt,
count(distinct case when prov = '10' then thru_dt else null end) as _10_cnt,
count(distinct case when prov = '34' then thru_dt else null end) as _34_cnt,
count(distinct case when prov = '13' then thru_dt else null end) as _13_cnt,
count(distinct case when prov = '49' then thru_dt else null end) as _49_cnt,
count(distinct case when prov = '02' then thru_dt else null end) as _02_cnt,
count(distinct case when prov = '04' then thru_dt else null end) as _04_cnt,
count(distinct case when prov = '73' then thru_dt else null end) as _73_cnt,
count(distinct case when prov = '47' then thru_dt else null end) as _47p_cnt,
count(distinct case when prov = 'C3' then thru_dt else null end) as _C3_cnt,
count(distinct case when prov = '65' then thru_dt else null end) as _65_cnt,
count(distinct case when prov = 'C1' then thru_dt else null end) as _C1_cnt,
count(distinct case when prov = '83' then thru_dt else null end) as _83_cnt,
count(distinct case when prov = '39' then thru_dt else null end) as _39_cnt,
count(distinct case when prov = '21' then thru_dt else null end) as _21_cnt,
count(distinct case when prov = '25' then thru_dt else null end) as _25_cnt,
count(distinct case when prov = '77' then thru_dt else null end) as _77_cnt,
count(distinct case when prov = '35' then thru_dt else null end) as _35_cnt,
count(distinct case when prov = '46' then thru_dt else null end) as _46_cnt,
count(distinct case when prov = '16' then thru_dt else null end) as _16_cnt,
count(distinct case when prov = '66' then thru_dt else null end) as _66_cnt,
count(distinct case when prov = '94' then thru_dt else null end) as _94_cnt,
count(distinct case when prov = '26' then thru_dt else null end) as _26p_cnt,
count(distinct case when prov = '44' then thru_dt else null end) as _44_cnt,
count(distinct case when prov = '63' then thru_dt else null end) as _63_cnt,
count(distinct case when prov = '14' then thru_dt else null end) as _14_cnt,
count(distinct case when prov = '81' then thru_dt else null end) as _81_cnt,
count(distinct case when prov = '64' then thru_dt else null end) as _64_cnt,
count(distinct case when prov = '68' then thru_dt else null end) as _68_cnt,
count(distinct case when prov = '90' then thru_dt else null end) as _90_cnt,
count(distinct case when prov = '92' then thru_dt else null end) as _92_cnt,
count(distinct case when prov = '72' then thru_dt else null end) as _72_cnt,
count(distinct case when prov = '09' then thru_dt else null end) as _09_cnt,
count(distinct case when prov = '03' then thru_dt else null end) as _03_cnt,
count(distinct case when prov in ('01','08','11') then thru_dt else null end) as pcp_cnt,
count(distinct case when prov not in ('22','30','32','43','44','45','47','54','58','59','60','61','63','69','74','A0','A1','A2','A3','A4','A5','A6') then thru_dt else null end) as op_cnt,
count(distinct prov) as dist_svc
from
(select c.dsysrtky, hcfaspcl as prov, thru_dt
from copd_2016 s 
inner join car_linek c
on s.dsysrtky = c.dsysrtky
where hcfaspcl is not null
and {cond}
UNION
select c.dsysrtky, REV_CNTR_RNDRNG_PHYSN_SPCLTY_CD as prov, thru_dt
from copd_2016 s 
inner join out_revenuek c
on s.dsysrtky = c.dsysrtky
where REV_CNTR_RNDRNG_PHYSN_SPCLTY_CD is not null
and {cond}
)subq
group by dsysrtky;
"""

outp_query = """
select dsysrtky,
count(distinct case when ccs = '228' then thru_dt else null end) as _228_cnt,
count(distinct case when ccs = '220' then thru_dt else null end) as _220_cnt,
count(distinct case when ccs = '206' then thru_dt else null end) as _206_cnt,
count(distinct case when ccs = '240' then thru_dt else null end) as _240_cnt,
count(distinct case when ccs = '234' then thru_dt else null end) as _234_cnt,
count(distinct case when ccs = '232' then thru_dt else null end) as _232_cnt,
count(distinct case when ccs = '193' then thru_dt else null end) as _193_cnt,
count(distinct case when ccs = '200' then thru_dt else null end) as _200_cnt,
count(distinct case when ccs = '170' then thru_dt else null end) as _170_cnt,
count(distinct case when ccs = '197' then thru_dt else null end) as _197_cnt,
count(distinct case when ccs = '178' then thru_dt else null end) as _178_cnt,
count(distinct case when ccs = '239' then thru_dt else null end) as _239_cnt,
count(distinct case when ccs = '38' then thru_dt else null end) as _38_cnt,
count(distinct case when ccs = '182' then thru_dt else null end) as _182_cnt,
count(distinct case when ccs = '179' then thru_dt else null end) as _179_cnt,
count(distinct case when ccs = '174' then thru_dt else null end) as _174_cnt,
count(distinct case when ccs = '198' then thru_dt else null end) as _198_cnt,
count(distinct case when ccs = '192' then thru_dt else null end) as _192_cnt,
count(distinct case when ccs = '177' then thru_dt else null end) as _177_cnt,
count(distinct case when ccs = '209' then thru_dt else null end) as _209_cnt,
count(distinct case when ccs = '196' then thru_dt else null end) as _196_cnt,
count(distinct case when ccs = '243' then thru_dt else null end) as _243_cnt,
count(distinct case when ccs = '155' then thru_dt else null end) as _155_cnt,
count(distinct case when ccs = '201' then thru_dt else null end) as _201_cnt,
count(distinct case when ccs = '203' then thru_dt else null end) as _203_cnt,
count(distinct case when ccs = '173' then thru_dt else null end) as _173_cnt,
count(distinct case when ccs = '237' then thru_dt else null end) as _237_cnt,
count(distinct case when ccs = '213' then thru_dt else null end) as _213_cnt,
count(distinct case when ccs = '218' then thru_dt else null end) as _218_cnt,
count(distinct case when ccs = '76' then thru_dt else null end) as _76_cnt,
count(distinct case when ccs = '180' then thru_dt else null end) as _180_cnt,
count(distinct case when ccs = '212' then thru_dt else null end) as _212_cnt,
count(distinct case when ccs = '70' then thru_dt else null end) as _70_cnt,
count(distinct case when ccs = '163' then thru_dt else null end) as _163_cnt,
count(distinct case when ccs = '15' then thru_dt else null end) as _15_cnt,
count(distinct case when ccs = '62' then thru_dt else null end) as _62_cnt,
count(distinct case when ccs = '54' then thru_dt else null end) as _54_cnt,
count(distinct case when ccs = '26' then thru_dt else null end) as _26_cnt,
count(distinct case when ccs = '5' then thru_dt else null end) as _5_cnt,
count(distinct case when ccs = '47' then thru_dt else null end) as _47_cnt,
count(distinct case when ccs = '171' then thru_dt else null end) as _171_cnt,
count(distinct case when ccs = '217' then thru_dt else null end) as _217_cnt,
count(distinct case when ccs = '214' then thru_dt else null end) as _214_cnt,
count(distinct case when ccs = '156' then thru_dt else null end) as _156_cnt,
count(distinct case when ccs = '100' then thru_dt else null end) as _100_cnt,
count(distinct case when line_icd_dgns_cd in ('J440','J441','J200','J201','J202','J203','J204','J205','J206','J207','J208','J209','J211','J218','J219','J210','J22','J069','J988') then thru_dt else null end) as aecopd_cnt,
'2016-12-31'- max(case when line_icd_dgns_cd in ('J440','J441','J200','J201','J202','J203','J204','J205','J206','J207','J208','J209','J211','J218','J219','J210','J22','J069','J988') then thru_dt else null end) as aecopd_days_since,
count(distinct case when betos in ('M1A','M1B','M2A','M2B','M5D','M6') then thru_dt else null end) as em_cnt,
count(distinct case when hcpcs_cd in ('90460','90461','90471','90472','90473','90474','90630','90653','90655','90657','90656','90658','90662','90672','90673','90674','90682','90685','90686','90687','90688','90689','90756','Q2035','90661','G0008','Q2034','Q2036','Q2037','Q2038','Q2039') then thru_dt else null end) as flu_cnt,
count(distinct case when hcpcs_cd in ('99401','99402','99403','99404','99411','99412','99406','99407') then thru_dt else null end) as tobac_cnt,
count(distinct betos) as betos_dist,
count(distinct prf_npi) as prf_npi_dist
from
	(select s.dsysrtky,hcpcs_cd,line_icd_dgns_cd,betos,prf_npi,ccs,thru_dt
			from copd_2016 s 
											inner join car_linek c
											on s.dsysrtky = c.dsysrtky
											where {cond}
	UNION
	select s.dsysrtky,hcpcs_cd,null as line_icd_dgns_cd,null as betos,rev_cntr_rndrng_physn_npi as prf_npi,ccs,thru_dt
	from copd_2016 s 
											inner join out_revenuek c
											on s.dsysrtky = c.dsysrtky
											where {cond}
	)subq
group by subq.dsysrtky;
"""


mbsf_query = """
select s.dsysrtky, 
CASE when sex= '1' then True else False end as is_male,
CASE when race = '1' then True else False end as race_white,
CASE when race = '2' then True else False end as race_black,
CASE when race = '5' then True else False end as race_hispanic,
CASE when race = '4' then True else False end as race_asian,
age,
CASE when dual_01 not in ('NA','99') then True else False end as medicaid,
CASE when hmo_mo > 0 then True else False end as hmo,
case when state_cd in ('07','20','22','30','41','47') then True else False end as reg1,
case when state_cd in ('31','33') then True else False end as reg2,
case when state_cd in ('08','09','21','39','49','51','73','80') then True else False end as reg3,
case when state_cd in ('01','10','11','18','25','34','42','44','68','69') then True else False end as reg4,
case when state_cd in ('03','05','12','29','55') then True else False end as reg9,
case when state_cd in ('14','15','23','24','36','52','72') then True else False end as reg5,
case when state_cd in ('16','17','26','28','70') then True else False end as reg7,
case when state_cd in ('06','27','35','43','46','53') then True else False end as reg8,
case when state_cd in ('02','13','38','50') then True else False end as reg10,
case when state_cd in ('04','19','32','37','45','67','71','74') then True else False end as reg6
from copd_2016 s 
left join mbsf c
on s.dsysrtky = c.dsysrtky
where {cond};"""


paid_amt_query = """
select dsysrtky,sum(pmt_amt) as total_paid
from 
(select i.dsysrtky,pmt_amt
 	FROM copd_2016 s 
	LEFT JOIN inp_claimsk i
	ON s.dsysrtky = i.dsysrtky
 	WHERE i.thru_dt < '2017-01-01'
 UNION
 select i.dsysrtky,pmt_amt
 	FROM copd_2016 s 
	LEFT JOIN car_claimsk i
	ON s.dsysrtky = i.dsysrtky
 	WHERE i.thru_dt < '2017-01-01'
 UNION
 select i.dsysrtky,pmt_amt
 	FROM copd_2016 s 
	LEFT JOIN dme_claimsk i
	ON s.dsysrtky = i.dsysrtky
 	WHERE i.thru_dt < '2017-01-01'
 UNION
 select i.dsysrtky,pmt_amt
 	FROM copd_2016 s 
	LEFT JOIN hha_claimsk i
	ON s.dsysrtky = i.dsysrtky
 	WHERE i.thru_dt < '2017-01-01'
 UNION
 select i.dsysrtky,pmt_amt
 	FROM copd_2016 s 
	LEFT JOIN out_claimsk i
	ON s.dsysrtky = i.dsysrtky
 	WHERE i.thru_dt < '2017-01-01'
 UNION
 select i.dsysrtky,pmt_amt
 	FROM copd_2016 s 
	LEFT JOIN snf_claimsk i
	ON s.dsysrtky = i.dsysrtky
 WHERE i.thru_dt < '2017-01-01'
)subq
group by dsysrtky
order by dsysrtky;
"""


