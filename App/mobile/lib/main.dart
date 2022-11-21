import 'package:flutter/material.dart';
import 'package:flutter_app_mustafa/home_page.dart';
import 'package:flutter_app_mustafa/landing_page.dart';
import 'package:flutter_app_mustafa/login_page.dart';
import 'package:flutter_app_mustafa/profile.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      //home: LandingPage(),
      //home: ProfilePage(),
      home: HomePage(),
    );
  }
}
