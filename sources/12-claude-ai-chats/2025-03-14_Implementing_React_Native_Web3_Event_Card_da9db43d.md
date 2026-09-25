# Implementing React Native Web3 Event Card

created: 2025-03-14T08:21:48.887380Z  uuid: da9db43d-3415-4163-96c7-ea5cc681171c  export: old
messages: 4  total_chars: 15396  human_chars: 48


---
**HUMAN** (2025-03-14T08:21):

这种在react native如何实现？

---
**ASSISTANT** (2025-03-14T08:22):

 我能帮您实现这个类似Web3活动卡片的React Native界面。这是一个活动详情页面，显示了一个Web3早餐活动的信息。

<antArtifact identifier="web3-event-card" type="application/vnd.ant.code" language="javascript" title="Web3活动卡片React Native实现">
import React from 'react';
import { View, Text, Image, StyleSheet, TouchableOpacity, ScrollView, SafeAreaView, StatusBar } from 'react-native';
import { Ionicons, FontAwesome5, MaterialCommunityIcons } from '@expo/vector-icons';

const Web3EventCard = () => {
  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" />
      
      {/* 顶部状态栏 */}
      <View style={styles.header}>
        <Text style={styles.time}>9:41</Text>
        <View style={styles.statusIcons}>
          <Ionicons name="cellular" size={16} color="#000" />
          <Ionicons name="wifi" size={16} color="#000" style={{marginLeft: 5}} />
          <Ionicons name="battery-full" size={20} color="#000" style={{marginLeft: 5}} />
        </View>
      </View>
      
      <ScrollView style={styles.scrollView}>
        {/* 活动封面图片 */}
        <Image 
          source={{uri: 'https://via.placeholder.com/350x350'}}
          style={styles.coverImage}
        />
        
        {/* 活动状态 */}
        <Text style={styles.attending}>Attending</Text>
        
        {/* 活动标题 */}
        <Text style={styles.title}>
          Web3 Growth Breakfast: Ideas, Insights, Espresso Shots
          <Text style={styles.rocketEmoji}> 🚀</Text>
        </Text>
        
        {/* 活动地点 */}
        <View style={styles.locationContainer}>
          <FontAwesome5 name="building" size={16} color="#333" />
          <Text style={styles.locationText}>Edge city</Text>
        </View>
        
        {/* 活动日期和时间 */}
        <View style={styles.dateTimeContainer}>
          <View style={styles.dateBox}>
            <Text style={styles.dateNumber}>29</Text>
            <Text style={styles.dateMonth}>Mar</Text>
          </View>
          
          <View style={styles.timeDetails}>
            <Text style={styles.dayText}>Tuesday</Text>
            <Text style={styles.timeText}>10:00 PM - 11:00PM UTC+5:00</Text>
          </View>
          
          <TouchableOpacity style={styles.calendarButton}>
            <Ionicons name="calendar-outline" size={24} color="#4CAF50" />
          </TouchableOpacity>
        </View>
        
        {/* 活动具体地点 */}
        <View style={styles.venueContainer}>
          <Ionicons name="location-sharp" size={24} color="#333" />
          <View style={styles.venueDetails}>
            <View style={styles.venueNameContainer}>
              <Text style={styles.venueChineseName}>大理市银桥镇白塔</Text>
              <Ionicons name="open-outline" size={16} color="#333" style={{marginLeft: 5}} />
            </View>
            <Text style={styles.venueEnglishName}>White Pagoda, Yinqiao Town, Dali City, China</Text>
          </View>
        </View>
      </ScrollView>
      
      {/* 底部提示 */}
      <View style={styles.bottomTip}>
        <Text style={styles.tipText}>
          活动由下往上弹出，{'\n'}下拉即可收起
        </Text>
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingVertical: 5,
  },
  time: {
    fontWeight: 'bold',
  },
  statusIcons: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  scrollView: {
    flex: 1,
    paddingHorizontal: 16,
  },
  coverImage: {
    width: '100%',
    height: 350,
    borderRadius: 8,
    marginTop: 16,
  },
  attending: {
    color: '#4CAF50',
    fontWeight: '600',
    marginTop: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginTop: 8,
    lineHeight: 32,
  },
  rocketEmoji: {
    fontSize: 20,
  },
  locationContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 16,
  },
  locationText: {
    marginLeft: 8,
    color: '#333',
  },
  dateTimeContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 24,
    marginBottom: 16,
  },
  dateBox: {
    width: 40,
    height: 50,
    backgroundColor: '#f5f5f5',
    borderRadius: 8,
    justifyContent: 'center',
    alignItems: 'center',
  },
  dateNumber: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  dateMonth: {
    fontSize: 12,
    color: '#666',
  },
  timeDetails: {
    marginLeft: 16,
    flex: 1,
  },
  dayText: {
    fontSize: 16,
    fontWeight: '500',
  },
  timeText: {
    fontSize: 14,
    color: '#666',
    marginTop: 4,
  },
  calendarButton: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: '#f0f9f0',
    justifyContent: 'center',
    alignItems: 'center',
  },
  venueContainer: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginTop: 8,
  },
  venueDetails: {
    marginLeft: 8,
    flex: 1,
  },
  venueNameContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  venueChineseName: {
    fontSize: 16,
    fontWeight: '500',
  },
  venueEnglishName: {
    fontSize: 14,
    color: '#666',
    marginTop: 4,
  },
  bottomTip: {
    position: 'absolute',
    right: 20,
    top: 120,
    backgroundColor: '#FFF9C4',
    padding: 12,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#FFD600',
  },
  tipText: {
    textAlign: 'center',
    fontSize: 14,
  },
});

export default Web3EventCard;
</antArtifact>

这个实现包含以下功能和元素：

1. 顶部状态栏(时间、信号、电池)
2. 活动封面图片(示例中使用了占位图)
3. "Attending"标签
4. 活动标题和火箭图标
5. "Edge city"地点标识
6. 日期和时间信息
7. 详细地点信息(中英文)
8. 右侧的提示框

要在React Native项目中使用这个组件，您需要：

1. 安装必要的依赖：
```
npm install @expo/vector-icons
```

2. 如果您想使用真实图片，请替换占位URL。

3. 根据您的应用需求调整样式和内容。

这个实现使用了React Native的基础组件，加上Expo的图标库来实现界面中的各种图标。您可以根据需要进一步优化和调整。

---
**HUMAN** (2025-03-14T08:23):

这个card 由下往上弹出， 下拉可以收起，这个怎么实现

---
**ASSISTANT** (2025-03-14T08:25):

 要实现卡片从下往上弹出并且可以通过下拉手势收起的效果，我们需要使用React Native的动画系统和手势处理库。这里我会使用`react-native-gesture-handler`和`react-native-reanimated`来实现这个效果。

<antArtifact identifier="web3-event-card-bottom-sheet" type="application/vnd.ant.code" language="javascript" title="带弹出和收起手势的Web3活动卡片">
import React, { useEffect } from 'react';
import { View, Text, Image, StyleSheet, TouchableOpacity, ScrollView, SafeAreaView, StatusBar, Dimensions } from 'react-native';
import { Ionicons, FontAwesome5 } from '@expo/vector-icons';
import Animated, { 
  useSharedValue, 
  useAnimatedStyle, 
  useAnimatedGestureHandler,
  withSpring,
  runOnJS
} from 'react-native-reanimated';
import { PanGestureHandler } from 'react-native-gesture-handler';

const { height: SCREEN_HEIGHT } = Dimensions.get('window');
const MAX_TRANSLATE_Y = -SCREEN_HEIGHT + 50;

const BottomSheetWeb3Card = ({ onClose }) => {
  // 控制底部卡片位置的共享值
  const translateY = useSharedValue(0);
  const context = useSharedValue({ y: 0 });
  
  // 当组件加载时，从底部弹出
  useEffect(() => {
    translateY.value = withSpring(MAX_TRANSLATE_Y, { damping: 15 });
  }, []);
  
  // 处理下拉手势
  const gestureHandler = useAnimatedGestureHandler({
    onStart: (_, ctx) => {
      ctx.startY = translateY.value;
    },
    onActive: (event, ctx) => {
      // 只允许向下拖拽（关闭方向）
      if (event.translationY > 0) {
        translateY.value = ctx.startY + event.translationY;
      }
    },
    onEnd: (event) => {
      // 如果拖拽速度很快或拖拽距离超过屏幕高度的20%，则关闭卡片
      if (event.velocityY > 500 || translateY.value > MAX_TRANSLATE_Y * 0.8) {
        translateY.value = withSpring(0, { damping: 15 });
        if (onClose) {
          runOnJS(onClose)();
        }
      } else {
        // 否则回弹到完全展开状态
        translateY.value = withSpring(MAX_TRANSLATE_Y, { damping: 15 });
      }
    },
  });

  const animatedStyle = useAnimatedStyle(() => {
    return {
      transform: [{ translateY: translateY.value }],
    };
  });

  return (
    <Animated.View style={[styles.container, animatedStyle]}>
      <PanGestureHandler onGestureEvent={gestureHandler}>
        <Animated.View style={styles.dragHandle}>
          <View style={styles.dragIndicator} />
        </Animated.View>
      </PanGestureHandler>
      
      <SafeAreaView style={styles.contentContainer}>
        <StatusBar barStyle="dark-content" />
        
        {/* 顶部状态栏 */}
        <View style={styles.header}>
          <Text style={styles.time}>9:41</Text>
          <View style={styles.statusIcons}>
            <Ionicons name="cellular" size={16} color="#000" />
            <Ionicons name="wifi" size={16} color="#000" style={{marginLeft: 5}} />
            <Ionicons name="battery-full" size={20} color="#000" style={{marginLeft: 5}} />
          </View>
        </View>
        
        <ScrollView 
          style={styles.scrollView}
          bounces={false}
          showsVerticalScrollIndicator={false}
        >
          {/* 活动封面图片 */}
          <Image 
            source={{uri: 'https://via.placeholder.com/350x350'}}
            style={styles.coverImage}
          />
          
          {/* 活动状态 */}
          <Text style={styles.attending}>Attending</Text>
          
          {/* 活动标题 */}
          <Text style={styles.title}>
            Web3 Growth Breakfast: Ideas, Insights, Espresso Shots
            <Text style={styles.rocketEmoji}> 🚀</Text>
          </Text>
          
          {/* 活动地点 */}
          <View style={styles.locationContainer}>
            <FontAwesome5 name="building" size={16} color="#333" />
            <Text style={styles.locationText}>Edge city</Text>
          </View>
          
          {/* 活动日期和时间 */}
          <View style={styles.dateTimeContainer}>
            <View style={styles.dateBox}>
              <Text style={styles.dateNumber}>29</Text>
              <Text style={styles.dateMonth}>Mar</Text>
            </View>
            
            <View style={styles.timeDetails}>
              <Text style={styles.dayText}>Tuesday</Text>
              <Text style={styles.timeText}>10:00 PM - 11:00PM UTC+5:00</Text>
            </View>
            
            <TouchableOpacity style={styles.calendarButton}>
              <Ionicons name="calendar-outline" size={24} color="#4CAF50" />
            </TouchableOpacity>
          </View>
          
          {/* 活动具体地点 */}
          <View style={styles.venueContainer}>
            <Ionicons name="location-sharp" size={24} color="#333" />
            <View style={styles.venueDetails}>
              <View style={styles.venueNameContainer}>
                <Text style={styles.venueChineseName}>大理市银桥镇白塔</Text>
                <Ionicons name="open-outline" size={16} color="#333" style={{marginLeft: 5}} />
              </View>
              <Text style={styles.venueEnglishName}>White Pagoda, Yinqiao Town, Dali City, China</Text>
            </View>
          </View>
          
          {/* 添加足够的空间使内容可滚动 */}
          <View style={{height: 100}} />
        </ScrollView>
        
        {/* 底部提示 */}
        <View style={styles.bottomTip}>
          <Text style={styles.tipText}>
            活动由下往上弹出，{'\n'}下拉即可收起
          </Text>
        </View>
      </SafeAreaView>
    </Animated.View>
  );
};

// 用于演示如何使用底部弹出卡片的包装组件
const App = () => {
  const [showCard, setShowCard] = React.useState(true);

  // 卡片关闭后的回调函数
  const handleClose = () => {
    setShowCard(false);
    console.log('Card closed');
    // 这里可以做额外的处理，如导航返回
  };

  return (
    <View style={styles.appContainer}>
      {showCard && <BottomSheetWeb3Card onClose={handleClose} />}
      {!showCard && (
        <TouchableOpacity 
          style={styles.openButton}
          onPress={() => setShowCard(true)}
        >
          <Text style={styles.openButtonText}>打开活动卡片</Text>
        </TouchableOpacity>
      )}
    </View>
  );
};

const styles = StyleSheet.create({
  appContainer: {
    flex: 1,
    backgroundColor: '#f0f0f0',
    justifyContent: 'center',
    alignItems: 'center',
  },
  openButton: {
    backgroundColor: '#4CAF50',
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 8,
  },
  openButtonText: {
    color: 'white',
    fontWeight: 'bold',
  },
  container: {
    position: 'absolute',
    left: 0,
    right: 0,
    bottom: -50, // 给底部留一点空间
    height: SCREEN_HEIGHT,
    backgroundColor: 'white',
    borderTopLeftRadius: 20,
    borderTopRightRadius: 20,
    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: -2,
    },
    shadowOpacity: 0.25,
    shadowRadius: 3.84,
    elevation: 5,
    zIndex: 999,
  },
  contentContainer: {
    flex: 1,
  },
  dragHandle: {
    width: '100%',
    height: 40,
    justifyContent: 'center',
    alignItems: 'center',
  },
  dragIndicator: {
    width: 60,
    height: 5,
    backgroundColor: '#D3D3D3',
    borderRadius: 5,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingVertical: 5,
  },
  time: {
    fontWeight: 'bold',
  },
  statusIcons: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  scrollView: {
    flex: 1,
    paddingHorizontal: 16,
  },
  coverImage: {
    width: '100%',
    height: 350,
    borderRadius: 8,
    marginTop: 16,
  },
  attending: {
    color: '#4CAF50',
    fontWeight: '600',
    marginTop: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginTop: 8,
    lineHeight: 32,
  },
  rocketEmoji: {
    fontSize: 20,
  },
  locationContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 16,
  },
  locationText: {
    marginLeft: 8,
    color: '#333',
  },
  dateTimeContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginTop: 24,
    marginBottom: 16,
  },
  dateBox: {
    width: 40,
    height: 50,
    backgroundColor: '#f5f5f5',
    borderRadius: 8,
    justifyContent: 'center',
    alignItems: 'center',
  },
  dateNumber: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  dateMonth: {
    fontSize: 12,
    color: '#666',
  },
  timeDetails: {
    marginLeft: 16,
    flex: 1,
  },
  dayText: {
    fontSize: 16,
    fontWeight: '500',
  },
  timeText: {
    fontSize: 14,
    color: '#666',
    marginTop: 4,
  },
  calendarButton: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: '#f0f9f0',
    justifyContent: 'center',
    alignItems: 'center',
  },
  venueContainer: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginTop: 8,
  },
  venueDetails: {
    marginLeft: 8,
    flex: 1,
  },
  venueNameContainer: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  venueChineseName: {
    fontSize: 16,
    fontWeight: '500',
  },
  venueEnglishName: {
    fontSize: 14,
    color: '#666',
    marginTop: 4,
  },
  bottomTip: {
    position: 'absolute',
    right: 20,
    top: 120,
    backgroundColor: '#FFF9C4',
    padding: 12,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#FFD600',
  },
  tipText: {
    textAlign: 'center',
    fontSize: 14,
  },
});

export default App;
</antArtifact>

要使用这个实现，您需要安装以下依赖：

```bash
npm install react-native-gesture-handler react-native-reanimated
```

这个实现的主要特点：

1. **底部弹出效果**：
   - 使用`react-native-reanimated`的共享值和动画函数
   - 组件加载时自动从底部弹出（使用`withSpring`实现弹簧效果）

2. **下拉关闭功能**：
   - 使用`PanGestureHandler`捕获用户的下拉手势
   - 只允许向下拖拽（关闭方向）
   - 基于用户拖拽的距离或速度决定是否关闭卡片或回弹

3. **视觉指示器**：
   - 顶部添加了一个拖动指示条，提示用户可以拖拽
   - 保留了原有的提示文本

4. **组件封装**：
   - 将卡片作为独立组件封装，提供`onClose`回调函数
   - 包含一个简单的App示例，展示如何使用这个卡片组件

5. **优化细节**：
   - 添加了阴影效果，使卡片看起来像是浮在屏幕上
   - 调整了圆角和动画参数，使交互更自然

如果您想在现有应用中集成，只需导入`BottomSheetWeb3Card`组件并在适当的时候显示它即可。这个组件使用了绝对定位覆盖在其他内容之上，所以它会自动占据整个屏幕。
