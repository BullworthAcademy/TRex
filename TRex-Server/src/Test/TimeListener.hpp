
#ifndef TIMELISTENER_H_
#define TIMELISTENER_H_

#include "../external.hpp"
#include "../connection.hpp"
#include "../util.hpp"
#include <iostream>
#include <chrono>
#include <ctime>

namespace concept{
namespace test{

class TimeListener: public ResultListener{
public:
    TimeListener();
    virtual ~TimeListener();

    virtual void handleResult(set<PubPkt *> &genPkts, double procTime);
    
private:
    std::chrono::time_point<std::chrono::system_clock> start;
    double elapsed;
    int numPkts;
};

} // test
} // concept
#endif /* TIMELISTENER_H_ */
