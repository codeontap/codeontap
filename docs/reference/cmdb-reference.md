# CMDB Reference

This reference provides an outline of the different classes of items within the CMDB. The classes form a hierarchy in the CMDB which defines your CodeOnTap deployment overall. Instances of classes are grouped together in collections and the overall collection is used to define the class

## Tenant

- **Description**
    A tenant represents an overall CodeOnTap deployment

## Account

- **Description**
    Represents a cloud providers highest billing entity, for AWS this would be an Account
- **Parent** Tenant

## Product

- **Description**
     A product defines an specific system in your IT Environment. We use product in the agile product sense so this should be scoped so that a product has a clearly defined product owner and team.

## Solution

- **Description**
    A solution defines the infrastructure in a product. Solutions describe each component and its configuration. A an instance of the solution is then deployed based on the environment and segment of a product

## Environment

- **Description**
    An environment represents a stage in the application life cycle, for example integration, preproduction, production would be three environments within a product. They represent the basic stages of an application life cycle, integration is to make sure new code introduced is technically working, preproduction is used for business testing and confirmation and production is the real world.

## Segment

- **Description**
    In more complicated products you might want to split up your infrastructure to make it easier to manage or to deploy resources in different locations. The components of a solution are deployed into a segment and each segment has its own solution.
- **Parent** Environment

## Tier

- **Description**
    A solution is divided up into tiers. A tier is a collection of components with a similar function or security boundary. For example you might have external load balancer tier which contains the internet facing load balancers, then an app tier would contain the containers which server your application. Tiers are primarily used in Network configuration. In this example the external load balancer tier would be available on the internet the app tier would be in a private network.
- **Parent** Solution

## Component

- **Description**
    A component represents an infrastructure unit such as a lambda function, load balancer or network. Components have a type which defines the configuration required for the component
- **Parent** - Tier

## Instance

- **Description**
    Within a solution your solution you might have a set of components which have very similar requirements, same type, same hardware etc but they have some slightly different settings. A component can have an instance which will use the components configuration by default and if more specific is set in the instance definition this will be overridden.
- **Parent** Component

## Version

- **Description**
    Similar to an instance you might want to have different versions of a component instance available. Like an instance any configuration applied at the version level will override the instance and component configuration. This is a common pattern in API deployments so that you can offer two versions of an API to users.
- **Parent** Instance
