# TurtleCoin-Krang aka Krang

This repo is where a Blockchain Automation Suite is going to live. The end goals are:

1. Completely scripted infrastructure provisioning
   1. 1st Digital Ocean then others Scaleway, Packet, GCE, AWS, etc
2. Completely scripted configuration management
   1. OS updates, Firewalls, IPs, Ports, Software, etc
3. Once the above is developed then combining that to run scenarios
   1. Test a daemon upgrade
   2. Test other daemon implementations
   3. Deploy a complete CI/CD/CD pipeline for TurtleCoin core suite (daemons, wallets, mining pools, etc)
   4. Run benchmarks on the blockchain itself
   5. Run benchmarks on the daemons catching regressions in performance and providing information to identify areas to optimise
4. Web app dashboard 
   1. Eventually we'll get here
   2. An all in one web app that can be used to launch anything above
   3. will provide knobs to turn things up and down
      - deploy 3 daemons to start
      - then add 4 more daemons
      - now add in 6 daemons on the next version
      - now start up wallets and send transactions
   4. will allow for custom scenarios that aren't covered by the existing suite
    
This is the plan. We are going to package everything into Docker containers and as such will build out a Docker build CI/CD/CD pipeline as well. Everything will be automated/scripted.

If you'd like to contribute join us on [#dev_general](https://discord.gg/JutXdZC) on the TurtleCoin Discord server

So far we are:
  + @SoreGums
  + @Slash-atello
  

# License

Copyright (C) 2018 Nicholas Orr, The TurtleCoin Developers

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see https://www.gnu.org/licenses/.      
