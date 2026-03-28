#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include <memory>

class SmartPointerNode : public rclcpp::Node
{
public:
  SmartPointerNode() : Node("smart_pointer_node")
  {
    // TODO: Create publisher using make_shared
    // TODO: Create timer with lambda callback
  }

private:
  void timer_callback()
  {
    // TODO: Create message using make_unique
    // TODO: Publish message
  }
  
  // TODO: Add member variables with smart pointers
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  // TODO: Use make_shared for node creation
  // TODO: Spin the node
  rclcpp::shutdown();
  return 0;
}