
import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Instagram Tools Web", layout="centered")
st.title("📱 Instagram Tools - Web Edition")
st.markdown("""
مرحبا بك! هذه نسخة الويب من أدوات إدارة Instagram. استعمل القائمة على اليسار للتنقل.
""")

option = st.sidebar.selectbox("🛠️ اختر الأداة:", [
    "📅 تخطيط المنشورات",
    "📊 حاسبة معدل التفاعل",
    "🏷️ جمع الهاشتاغ",
    "🔍 تحليل المنافسين",
    "🗂️ تنظيم المحتوى",
    "👁️‍🗨️ عداد المشاهدات"
])

if option == "📅 تخطيط المنشورات":
    st.subheader("📅 تخطيط منشور جديد")
    date = st.date_input("📆 التاريخ", datetime.date.today())
    time = st.time_input("⏰ الوقت", datetime.datetime.now().time())
    caption = st.text_area("📝 نص المنشور")
    hashtags = st.text_input("🏷️ الهاشتاغات")
    if st.button("💾 حفظ الخطة"):
        st.success("✅ تم حفظ المنشور")

elif option == "📊 حاسبة معدل التفاعل":
    st.subheader("📊 حساب معدل التفاعل")
    likes = st.number_input("👍 الإعجابات", 0)
    comments = st.number_input("💬 التعليقات", 0)
    followers = st.number_input("👥 المتابعين", 1)
    if st.button("📈 احسب"):
        rate = ((likes + comments) / followers) * 100
        st.info(f"📊 معدل التفاعل: {rate:.2f}%")

elif option == "🏷️ جمع الهاشتاغ":
    st.subheader("🏷️ اقتراح هاشتاغات")
    topic = st.text_input("🔍 الموضوع")
    if st.button("🎯 عرض الهاشتاغات"):
        tags = [f"#{topic}", f"#{topic}life", f"#{topic}daily"]
        st.code(" ".join(tags))

elif option == "🔍 تحليل المنافسين":
    st.subheader("🔍 تحليل حساب")
    username = st.text_input("👤 اسم المستخدم")
    if st.button("📊 تحليل"):
        st.warning("📌 سيتم إضافة التحليل لاحقًا عبر API")

elif option == "🗂️ تنظيم المحتوى":
    st.subheader("🗂️ رفع الملفات")
    uploads = st.file_uploader("📤 حمل الصور أو الفيديوهات", accept_multiple_files=True)
    for f in uploads:
        st.success(f"✅ تم رفع: {f.name}")

elif option == "👁️‍🗨️ عداد المشاهدات":
    st.subheader("👁️ عرض مشاهدات ريل")
    reel = st.text_input("🎬 أدخل رابط الريل")
    if st.button("👁️ عرض"):
        st.warning("🚧 الميزة غير مفعلة حاليًا، جاري التطوير")
