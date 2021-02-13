# What is Ghost?

A fullstack, modern publishing platform.

fullstack?
- incorporates the frontend and backend
- backend: headless cms
- frontend: collection of themes
- includes a built in admin site for editing and managing content
- handles SEO
- integrates with many other tools like Zapier, Mailchimp, Stripe, Slack, Twitter, ...
- offer a paid platform as a service

modern?
- built on nodejs. By comparison, Wordpress is build on PHP. No hate against PHP, but I prefer to use javascript.

publishing platform?

audience: targeted at small content creators and "indie hackers" who want to build an online audience
    - streamlines setting up subscriptions for paid content

open source

## customization

- Use handlebars templating
- [starter theme](https://github.com/tryghost/starter) available in a repo

## content api
- rest api as well as a Javascript client library

# What is Google Cloud Platform?

- GCP provides google's internal infrastructure to developers as a service
- Range of products. Including a PaaS called app engine and a IaaS called compute engine
- Reasons for using:
    - cheap compared to running your own server
    - some maintainance is taken care of for you
    - autoscaling. good for companies that have periods of activity and other periods of downtime
- alternatives:
    - virtual private hosting
    - colocated hosting
    - on-premises hosting
- billing is more flexible. you are billed for what you use
- cloud services are abstractions over physical computers
- summary:
    - a cloud is a collection of services that abstract away computer infrastructure
    - using a cloud is a good fit if you
        1. Don't want to manage your own servers
        2. have needs that change frequently, or are unknown
    - using a cloud is a bad fit if your usage is steady over a long period of time

## What is a datacenter?
- a datacenter is a physical location where the computers that a cloud runs on are kept
- isolation levels and fault tolerance
    - zone: smallest unit in which a resource can exist. Think of a zone as a single data center
    - region: a collection of zones. think of a region as a city
    - isolation level / control plane: the thing that would have to go down to take your sevice down with it
    - zonal vs. regional vs. multiregional vs. global
    - multiregional is usally good enough to protect against natural disasters that may wipe out the datacenters in a single region.
- security implications:
    - using a cloud provider means trading control over assets (data or source code) for flexibility and lower cost
    - security concerns:
        - privacy: only authorized people should be able to access the resouces
        - availablility: the resources should always be accessible to people
        - durability: the resources should never get corrupted or go missing
- all GCP services encrypt data before sending it
- resource isolation and performance
    - computers in a datacenter are split into smaller virtual machines
    - noisy neighbor problem: when someone using another VM on the same physical machine runs a CPU intensive workload and steals computing cycles from other VMS on the same physical machine
    - Borg - a system that allocates work to VMS at Google
- replication: backup copy of a database
    - principle: avoid having a single point of failure in your production systems
    - read only replicas: do not allow inserts, updates, deletes
        - allow horizontal scaling
    - failover replica: exact copy of the primary database, ready to switch in if it fails
- Horizontal vs. Vertical Scaling
    - Horizontal scaling: add more machines to the resource pool
    - Vertical scaling: add more power (CPU, RAM) to an existing machine


## Storage
### Cloud SQL
- cloud sql is managed relational storage
- setting up cloud sql for production
- vms in compute engine live on a virtual network that assigns IPs from a special subnet for the project
- SSL for queries
    - SSL connections as a client require 3 things:
        - the server's CA certificate
        - a client certificate
        - a client private key
    - need to set this up for database queries in production!
- need to set a maintainence schedule for production databases
- in VM, mysql config file is `my.cnf`
- storage capacity:
# Setting up the blog

## System layout

- mysql database
- nginx web server
- ghost cms

## Request lifecycle

## What goes on between requests? Admin page and CMS.



1. Sign up for a GCP account
2. Create a project for the blog
3. install gcloud SDK
    - the SDK is a command line tool that allows you to perform actions that would normally be performed in a web browser, but through the command line instead.
