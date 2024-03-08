FROM apache/airflow:2.6.1
RUN airflow db init
CMD ["airflow", "webserver", "-p", "8080"]
