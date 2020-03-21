###### windows OS

- windows NT: family of OS, first released 1993, NT doesnt really have any meaning used to meaen new technology.
- windows service: background computer process, similar to oa unix daemon. run by the windows service control manager. eg configure to run in bg when system started or @manual or @event. command line tool is sc.exe to manage windows services.
    + service wrapper: computer program that wraps (wrap another function in code to allow to be used with another software interface) arbitrary programs
        * NSSM is an example. it calls itself non sucking because it can handle program failing/ shutdown, whereas others may not do that. 
        * srvany