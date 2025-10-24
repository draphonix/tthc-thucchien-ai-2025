from openai import OpenAI
import base64
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"), base_url=os.getenv("BASE_URL"))

PROMPT= """
Bạn là một Biên kịch chuyên nghiệp chuyên viết kịch bản tin tức video cho các chương trình truyền hình. Mục tiêu chính của bạn là tạo ra các kịch bản hấp dẫn, giàu thông tin và súc tích, tuân thủ các tiêu chuẩn phát sóng và thu hút sự chú ý của khán giả.

**Trách nhiệm chính:**

*   **Rõ ràng và Súc tích:** Viết kịch bản dễ hiểu, tránh biệt ngữ và sự phức tạp không cần thiết. Mọi từ ngữ đều phải có giá trị.
*   **Chính xác và Khách quan:** Đảm bảo tất cả thông tin thực tế đều chính xác và được trình bày một cách khách quan, duy trì tính toàn vẹn của báo chí.
*   **Kể chuyện:** Xây dựng các câu chuyện hấp dẫn trình bày các sự kiện tin tức một cách lôi cuốn, phù hợp với phương tiện truyền thông hình ảnh.
*   **Định dạng phát sóng:** Tuân thủ các định dạng kịch bản tin tức truyền hình tiêu chuẩn, bao gồm các tín hiệu cho hình ảnh (video, đồ họa), âm thanh (soundbites, âm thanh tự nhiên) và cách trình bày của phóng viên/người dẫn chương trình.
*   **Nhịp độ và Lưu loát:** Phát triển kịch bản với nhịp điệu và sự lưu loát tự nhiên bổ sung cho các yếu tố hình ảnh và giữ chân người xem.
*   **Khả năng thích ứng:** Sẵn sàng điều chỉnh kịch bản nhanh chóng dựa trên tin tức nóng hổi, thông tin mới hoặc thay đổi biên tập.
*   **Đối tượng mục tiêu:** Điều chỉnh ngôn ngữ và giọng điệu để phù hợp với đối tượng khán giả tin tức truyền hình rộng lớn.

**Khi viết, hãy xem xét những điều sau:**

*   **Hình ảnh trước tiên:** Hãy nghĩ về những gì người xem sẽ thấy trên màn hình và cách kịch bản có thể nâng cao hoặc giải thích những hình ảnh đó.
*   **Soundbites:** Tích hợp soundbites một cách hiệu quả, đảm bảo chúng tăng thêm giá trị và được giới thiệu đúng cách.
*   **Hạn chế thời gian:** Lưu ý đến giới hạn thời gian nghiêm ngặt cho mỗi phân đoạn và câu chuyện.
*   **Kêu gọi hành động/Các bước tiếp theo (nếu có):** Đối với một số câu chuyện, hãy xem xét liệu có bước tiếp theo tự nhiên hoặc lời kêu gọi hành động nào dành cho người xem hay không.
*   **Kịch bản dành cho video 60 giây, gồm phần mở đầu ấn tượng
*   **Kịch bản phải được viết để cho dẫn chương trình đọc.
*   **Trả về dưới định dạng Markdown
Đầu ra của bạn phải là một kịch bản tin tức được cấu trúc tốt, sẵn sàng phát sóng dựa trên chủ đề và chi tiết được cung cấp.

"""

USER_PROMPT = """
Ứng dụng AI vào camera giao thông

1.  **Phát hiện và Xử lý Vi phạm Giao thông Chính xác & Tự động:**
    *   **Phát hiện đa dạng vi phạm:** AI có thể nhận diện nhiều loại vi phạm hơn camera thường, bao gồm: vượt đèn đỏ, đi sai làn, lấn vạch, dừng đỗ sai quy định, đi ngược chiều, không đội mũ bảo hiểm, không thắt dây an toàn, sử dụng điện thoại khi lái xe, chạy quá tốc độ, rẽ sai làn, lùi xe trái phép, thậm chí là xe không có biển số hoặc biển số bị che khuất.
    *   **Độ chính xác cao:** AI sử dụng các thuật toán học sâu để phân tích hình ảnh và video, giảm thiểu lỗi của con người và sai sót trong quá trình xác định vi phạm.
    *   **Tự động hóa hoàn toàn:** Từ việc phát hiện, chụp ảnh/quay video bằng chứng, đến nhận dạng biển số (OCR), tất cả đều có thể được tự động hóa, giảm gánh nặng cho lực lượng chức năng.

2.  **Quản lý Lưu lượng Giao thông Hiệu quả:**
    *   **Đếm và phân loại phương tiện:** AI có thể đếm chính xác số lượng xe cộ (ô tô, xe máy, xe buýt, xe tải) và thậm chí là người đi bộ, cung cấp dữ liệu chi tiết về lưu lượng.
    *   **Phân tích mật độ và tắc nghẽn:** Xác định các khu vực có mật độ xe cao, phát hiện sớm tình trạng ùn tắc để đưa ra các biện pháp can thiệp kịp thời (ví dụ: điều chỉnh đèn tín hiệu, cảnh báo lái xe).
    *   **Tối ưu hóa đèn tín hiệu giao thông:** Dựa trên dữ liệu thời gian thực về lưu lượng, AI có thể tự động điều chỉnh chu kỳ đèn xanh/đỏ tại các nút giao thông để tối ưu hóa dòng chảy, giảm thời gian chờ và ùn tắc.
    *   **Đề xuất lộ trình thay thế:** Khi phát hiện tắc nghẽn hoặc sự cố, hệ thống có thể đề xuất các lộ trình thay thế cho người lái thông qua ứng dụng hoặc biển báo điện tử.

3.  **Nâng cao An toàn Giao thông:**
    *   **Phát hiện sớm tai nạn và sự cố:** AI có thể nhận diện các tình huống bất thường như va chạm, xe dừng đột ngột, vật cản trên đường, hoặc xe đi ngược chiều, và tự động gửi cảnh báo đến trung tâm điều hành để phản ứng nhanh chóng.
    *   **Cảnh báo hành vi nguy hiểm:** Ngoài các vi phạm rõ ràng, AI có thể nhận diện các hành vi lái xe nguy hiểm khác (ví dụ: lạng lách, đánh võng) để cảnh báo hoặc ghi nhận.
    *   **Bảo vệ người đi bộ và xe đạp:** Phát hiện người đi bộ băng qua đường sai quy định hoặc các tình huống tiềm ẩn nguy hiểm giữa phương tiện và người đi bộ/xe đạp.
    *   **Hỗ trợ phương tiện khẩn cấp:** Ưu tiên luồng giao thông (mở đèn xanh) cho xe cứu hỏa, cứu thương khi chúng tiếp cận nút giao thông.

4.  **Thu thập Dữ liệu và Phân tích Chuyên sâu:**
    *   **Kho dữ liệu khổng lồ:** Camera AI thu thập một lượng lớn dữ liệu có giá trị về hành vi người tham gia giao thông, lưu lượng, thời gian di chuyển, và các điểm nóng vi phạm.
    *   **Phân tích xu hướng dài hạn:** Dữ liệu này là cơ sở quan trọng để các nhà quy hoạch đô thị và giao thông phân tích xu hướng, dự báo, đưa ra quyết định về mở rộng đường, xây cầu, đặt thêm đèn tín hiệu, hoặc thay đổi quy tắc giao thông.
    *   **Đánh giá hiệu quả chính sách:** Đo lường tác động của các chính sách giao thông mới hoặc các chiến dịch an toàn giao thông.

5.  **Tối ưu hóa Hoạt động và Giảm Chi phí:**
    *   **Giảm sự can thiệp của con người:** Tự động hóa quá trình giám sát và xử lý vi phạm giúp giảm số lượng nhân sự cần thiết và giảm thiểu sai sót do con người.
    *   **Bằng chứng minh bạch:** Cung cấp bằng chứng vi phạm rõ ràng, khó chối cãi, giúp quá trình xử phạt trở nên minh bạch và hiệu quả hơn.
    *   **Hoạt động 24/7:** Camera AI có thể hoạt động liên tục mà không bị mệt mỏi hay ảnh hưởng bởi các yếu tố bên ngoài.
    *   **Hiệu quả phòng ngừa:** Sự hiện diện của camera AI và khả năng phát hiện vi phạm cao sẽ nâng cao ý thức tuân thủ luật giao thông của người dân.

Tóm lại, việc ứng dụng AI vào camera giao thông không chỉ đơn thuần là "ghi hình" mà là một hệ thống thông minh toàn diện, giúp quản lý giao thông hiệu quả hơn, nâng cao an toàn, giảm thiểu ùn tắc và cung cấp dữ liệu giá trị cho quy hoạch đô thị trong tương lai.

Ứng dụng AI vào dịch vụ công
1.  **Tăng cường hiệu quả và tốc độ xử lý:**
    *   **Tự động hóa quy trình:** AI có thể tự động hóa các tác vụ lặp đi lặp lại và tốn thời gian như xử lý hồ sơ, cấp phép, xác minh thông tin. Điều này giúp giảm đáng kể thời gian chờ đợi cho người dân và giải phóng nhân lực để tập trung vào các công việc phức tạp hơn.
    *   **Xử lý dữ liệu lớn:** AI có khả năng phân tích và xử lý lượng lớn dữ liệu nhanh chóng, từ đó đưa ra các kết quả hoặc quyết định tức thì, ví dụ như kiểm tra tính hợp lệ của đơn đăng ký.

2.  **Cải thiện chất lượng dịch vụ và độ chính xác:**
    *   **Giảm thiểu sai sót:** AI loại bỏ lỗi do con người gây ra trong quá trình nhập liệu, tính toán hoặc xử lý thông tin, đảm bảo độ chính xác cao hơn.
    *   **Phân tích sâu sắc:** AI có thể phân tích các mẫu dữ liệu để dự đoán nhu cầu, phát hiện các vấn đề tiềm ẩn và đưa ra các khuyến nghị cải thiện dịch vụ.

3.  **Nâng cao trải nghiệm người dân (Citizen Experience):**
    *   **Hỗ trợ 24/7:** Chatbot và trợ lý ảo AI có thể cung cấp thông tin, trả lời câu hỏi và hướng dẫn người dân làm thủ tục mọi lúc mọi nơi, không giới hạn giờ hành chính.
    *   **Cá nhân hóa dịch vụ:** AI có thể phân tích lịch sử tương tác và nhu cầu của từng người dân để cung cấp thông tin, dịch vụ hoặc lời khuyên phù hợp, chủ động nhắc nhở về các nghĩa vụ (ví dụ: gia hạn giấy tờ) hoặc quyền lợi.
    *   **Dễ dàng tiếp cận:** Cung cấp các giao diện thân thiện, đa ngôn ngữ hoặc hỗ trợ người khuyết tật thông qua công nghệ nhận diện giọng nói, chuyển văn bản thành giọng nói.

4.  **Tối ưu hóa nguồn lực và tiết kiệm chi phí:**
    *   **Giảm chi phí vận hành:** Tự động hóa giúp giảm nhu cầu về nhân lực cho các tác vụ đơn giản, từ đó tiết kiệm chi phí lương bổng và đào tạo.
    *   **Phân bổ nguồn lực hiệu quả:** AI có thể dự đoán nhu cầu dịch vụ ở các khu vực khác nhau, giúp chính phủ phân bổ nguồn lực (nhân sự, vật tư, hạ tầng) một cách thông minh và hiệu quả hơn.
    *   **Ngăn chặn gian lận:** AI có thể phát hiện các hành vi gian lận trong các chương trình phúc lợi xã hội, khai báo thuế hoặc các giao dịch công, giúp bảo vệ ngân sách nhà nước.

5.  **Hỗ trợ ra quyết định dựa trên dữ liệu:**
    *   **Phân tích dự đoán:** AI có thể phân tích dữ liệu lịch sử để dự đoán các xu hướng tương lai, giúp các nhà hoạch định chính sách đưa ra quyết định sáng suốt hơn trong quy hoạch đô thị, quản lý giao thông, y tế công cộng hoặc ứng phó thiên tai.
    *   **Đánh giá tác động chính sách:** AI có thể mô phỏng và đánh giá tác động tiềm năng của các chính sách mới trước khi triển khai rộng rãi.

6.  **Tăng cường minh bạch và trách nhiệm giải trình:**
    *   **Theo dõi và giám sát:** AI có thể giúp theo dõi và giám sát các quy trình dịch vụ công, đảm bảo tính minh bạch và công bằng.
    *   **Báo cáo tự động:** Tự động tạo báo cáo về hiệu suất dịch vụ, giúp công chúng và các bên liên quan dễ dàng nắm bắt thông tin và đánh giá hiệu quả hoạt động.

7.  **An ninh và an toàn:**
    *   **Phát hiện mối đe dọa:** AI có thể được sử dụng để phát hiện các mối đe dọa an ninh mạng, giám sát an toàn công cộng (ví dụ: phân tích video giám sát để phát hiện sự cố), hoặc hỗ trợ công tác cứu hộ khẩn cấp.

Tóm lại, việc ứng dụng AI vào dịch vụ công không chỉ đơn thuần là hiện đại hóa mà còn là một bước nhảy vọt trong việc nâng cao chất lượng quản lý nhà nước, cải thiện chất lượng cuộc sống cho người dân và xây dựng một nền hành chính công hiệu quả, minh bạch và lấy người dân làm trung tâm.

Ứng dụng AI tạo ứng dụng hỗ trợ đồng bào gặp lũ lụt ngay trong đêm.
Độ phủ sóng cao
Tốc độ
Tương tác 
Chính xac
Giữa đêm tâm lũ đổ bộ miền Bắc, hàng trăm bài viết cầu cứu từ Thái Nguyên xuất hiện dày đặc trên mạng xã hội, chị Nguyễn Thị Mai Anh, cựu sinh viên khóa 7 ngành Quản trị kinh doanh, Trường Đại học FPT, cùng đồng nghiệp đã nhanh chóng bắt tay tạo một nền tảng số tổng hợp dữ liệu cứu hộ khẩn cấp, giúp tập trung và trực quan hóa thông tin cầu cứu của người dân vùng lũ.



Chương trình thực chiến AI
Thu hút hơn 100 đội thi đến từ các tỉnh thành
Tìm kiếm nhân tài A.I quốc gia
Nhân tài phát triển công nghệ nền tảng A.I.
Nhân tài phát triển hệ sinh thái ứng dụng A.I.


Xây dựng mô hình LLM/SLM tiếng Việt quốc gia
Khởi động từ A.I Thực Chiến để xây dựng nền tảng mô hình nền tảng A.I ngôn ngữ lớn (LLM), ngôn ngữ nhỏ (SLM) tiếng Việt, cải tiến theo từng năm cho quốc gia.
Huy động nguồn lực quốc gia (nhà nước, doanh nghiệp, startup, nhà phát triển, nhà nghiên cứu,...).
Hướng tiếp cận để tạo đột phá và làm chủ công nghệ A.I theo NQ 57.
Xây dựng HST ứng dụng và startup A.I/LLM cho Quốc gia
Phát triển HST ứng dụng A.I/LLM dựa trên cơ sở dữ liệu quốc gia Make in Vietnam.
Phát triển hệ sinh thái vườn ươm startup cho A.I/LLM quốc gia.

Lan tỏa tinh thần học và ứng dụng A.I trong cộng đồng
Nâng cao nhận thức và kỹ năng A.I cho thế hệ trẻ.
Đào tạo và phát triển đội ngũ nhân lực A.I chất lượng cao.
Xây dựng văn hóa sử dụng A.I một cách có trách nhiệm & hiệu quả.

"""
response = client.chat.completions.create(
    model="gemini-2.5-pro",
    messages=[
        {"role": "system", "content": PROMPT},
        {
            "role": "user",
            "content": USER_PROMPT,
        }
    ],
    reasoning_effort="high",
)

print(response.choices[0].message.content)
