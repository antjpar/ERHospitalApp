# Queue-Api

## Building docker image

```$ docker build -t api .```

## Run built docker image

```$ docker run --rm -p 8080:8080 api```


## API Documentation ##
### Public Data Types ###
* Appointment ID: UUID as string
* Hospital ID: UUID as string
* Priority: Integer between 0 and 9

### Internal Data Types ###
Waitinglist consisting of multiple (10) queues for priorities. New entries are appended in queues. Entries are processed from the top of a queue going down (FIFO). Queues of higher priorities are processed first. Queues are processed as soon as there is no entry with waiting status in any queue with a higher priority.

[ collections.deque([${Appointment ID}, ${status}],...), ... ]

Waitingtime

Attributs of Appointment ID
status (Enumeration)
Waitung: The patient is waiting.
Processing: A consultant is processing the appointment (seeing the patient)
Ended: The consultation has ended. The patient has been dismissed.

### API ###
1. Warteschlange
   1. Get Queue Length and Wait Time
      * Entrypoint: expected_apt_wait
      * Param: None
      * Return: Array showing the number of entries in all queues and the approximate waiting time in minutes: [${Number of Entries}, ${Waiting Time}].
   2. Create appointment
      * Entrypoint: create_apt?priority=${Priority}
      * Param: priority Priority queue to put appointment into. Priority is a number in the interval [0, 9]. Default 0
      * Return: UUID "Appointment ID" of the new appointment if appointment was successfully scheduled.
   3. Get an Appointment's Waiting Time
      * Entrypoint: apt_status?id=${Appointment ID}
      * Param: id Appointment ID
      * Return: Array showing the number of entries in the queue ahead of the given appointment and the approximate waiting time in minutes: [${Waiting Position}, ${Waiting Time}]. HTTP 404 if the appointment does not exist.
      * Example:
   4. Start an Apointment
      * Entrypoint: start_apt?id=${Appointment ID}
      * Param: id Appointment ID
      * Return: "true" if the given appointment had not been started and its status was successfully transitioned to have started. "false" if the given appointment has already been started. HTTP 404 if the appointment does not exist.
      * Example:
   5. End Appointment
      * Entrypoint: end_apt?id=${Appointment ID}
      * Param: id Appointment ID
      * Return: "true" if appointment exists and has been set to have ended. HTTP 404 if appointment does not exist
   6. Get All Appointments for Hospital
      * Entrypoint: all_appointments
      * Param: None
      * Return: Map of priorities to queues. Queues as an array containing all entries with their status as tupel.
      {0: [[${Appointment ID}, ${Status}], ... ], 1: [[${Appointment ID}, ${Status}], ... ], ... 9: []}
2. Rückruf (Audio oder Video)
   1. Get Queue Length and Wait Time
       * Entrypoint: expected_call_wait
       * See documentation for apointment.
   2. Create Video Callback Request
       * Entrypoint: request_call?priority=${Priority}
       * See documentation for apointment.
   3. Get a Callback Request's Waiting Time
       * Entrypoint: call_status?id=${Appointment ID}
       * See documentation for apointment.
   4. Answer Call for Hospital
       * Entrypoint: start_call?id=${Appointment ID}
       * See documentation for apointment.
   5. Call finished
       * Entrypoint: call_finished?id=${Appointment ID}
       * See documentation for apointment.
   6. Get All Callback Requests for Hospital
       * Entrypoint: all_calls
       * See documentation for apointment.
   7. Get video call URL
       * Entrypoint: call_url?id=${Appointment ID}
       * Param:  id Appointment ID
       * Return: URL String, for example "https://meet.jit.si/....".
3. get hospitals
   * Entrypoint: get_hospitals
   * Param: None
   * Return: [{"name": ${Hospital name}, "id": ${Hospital ID}}, ...]
