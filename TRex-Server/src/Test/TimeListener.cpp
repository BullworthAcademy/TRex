/*
 * Copyright (C) 2011 Francesco Feltrinelli <first_name DOT last_name AT gmail DOT com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 */

#include "TimeListener.hpp"

using namespace concept::test;
using namespace concept::util;


double elapsed = 0;
int numPkts = 0;

TimeListener::TimeListener():
    start(std::chrono::system_clock::now()), elapsed(0), numPkts(0)
{}

TimeListener::~TimeListener(){
}

void TimeListener::handleResult(set<PubPkt *> &genPkts, double procTime){
    std::chrono::time_point<std::chrono::system_clock> now;
    
    if (elapsed >= 10.0){
        std::cout << "Throughput rate: " << numPkts/elapsed << "Pkt/s\n";
        elapsed = 0;
        numPkts = 0;
    } else {
        now = std::chrono::system_clock::now();
        std::chrono::duration<double> elapsed_seconds = now - start;
        elapsed = elapsed_seconds.count();
        numPkts += genPkts.size();
    }
    
    std::cout << "Latency: " << procTime << "ms\n";
}

