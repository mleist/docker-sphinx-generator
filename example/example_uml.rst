Graph Example
=============

Components
----------

.. uml::
   :caption: Caption with **bold** and *italic*
   :width: 150mm

   package "Some Group" {
     HTTP - [First Component]
     [Another Component]
   }

   node "Other Groups" {
     FTP - [Second Component]
     [First Component] --> FTP
     json JSON {
       "fruit":"Apple",
       "size":"Large",
       "color": ["Red", "Green"]
     }
   }

   cloud {
     [Example 1]
     note right
       ""monospaced""
       ""12 text 90""
       ""1234567890""
     end note
   }


   database "MySql" {
     folder "This is my folder" {
       [Folder 3]
     }
     frame "Foo" {
       [Frame 4]
       note right
         normal text
         12 text 901
         12345678901
       end note
     }
   }


   [Another Component] --> [Example 1]
   [Example 1] --> [Folder 3]
   [Folder 3] --> [Frame 4]


Icons
-----

.. uml::
   :caption: Example Icons
   :width: 100mm

   !include <logos/flask>
   !include <logos/kafka>
   !include <logos/kotlin>
   !include <logos/cassandra>
   !include <logos/bash>
   !include <logos/jetbrains>

   rectangle "<$flask>\nwebapp" as webapp
   queue "<$kafka>" as kafka
   rectangle "<$kotlin>\ndaemon" as daemon
   database "<$cassandra>" as cassandra

   rectangle "<$bash>" as bash
   rectangle "<$jetbrains>" as jetbrains

   webapp -> kafka
   kafka -> daemon
   daemon --> cassandra
   daemon --> bash
   daemon -> jetbrains
   bash -> cassandra
   jetbrains --> cassandra



Azure Icons
-----------

.. uml::
   :caption: Azure Example Graph
   :name: fig-azure

   !include <azure/AzureCommon>
   !include <azure/Analytics/AzureEventHub>
   !include <azure/Analytics/AzureStreamAnalyticsJob>
   !include <azure/Databases/AzureCosmosDb>

   skinparam shadowing true
   left to right direction

   agent "Device Simulator" as devices #fff

   AzureEventHub(fareDataEventHub, "Fare Data", "PK: Medallion HackLicense VendorId; 3 TUs")
   AzureEventHub(tripDataEventHub, "Trip Data", "PK: Medallion HackLicense VendorId; 3 TUs")
   AzureStreamAnalyticsJob(streamAnalytics, "Stream Processing", "6 SUs")
   AzureCosmosDb(outputCosmosDb, "Output Database", "1,000 RUs")

   devices --> fareDataEventHub
   devices --> tripDataEventHub
   fareDataEventHub --> streamAnalytics
   tripDataEventHub --> streamAnalytics
   streamAnalytics --> outputCosmosDb

