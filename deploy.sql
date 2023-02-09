CREATE SERVICE flask
  MIN_INSTANCES = 1
  MAX_INSTANCES = 1
  COMPUTE_POOL = TESTPOOL_SNOWCAT_STANDARD_4_CPU
  SPEC = @deploy/flask.yaml;

desc service flask;

create or replace function echo(v varchar)
  returns varchar
  service=flask!flask;
